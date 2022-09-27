import sys
import re
import base64
import json
import pathlib

from algosdk.v2client.algod import AlgodClient


algod = AlgodClient('', 'https://testnet-api.algonode.cloud', headers={'User-Agent': 'algosdk'})


def compile(teal):
    response = algod.compile(teal)
    return base64.b64decode(response['result']), response['hash'].encode()


def replace_variables_and_compile(teal):
    int_placeholder = 0xf000000000000000
    lookup = {}
    template_variables = sorted(set(re.findall('int (TMPL_[A-Z0-9_]+)', teal))) # We only handle ints for now
    for v in template_variables:
        lookup[v] = int_placeholder # For the moment we just hope this int doesn't already appear in the code
        teal = teal.replace(v, str(int_placeholder))
        int_placeholder += 1
    bytecode, address = compile(teal)
    variables = {}
    for v in lookup:
        p = lookup[v]
        placeholder_bytes = encode_varint(p)
        index = bytecode.index(placeholder_bytes)
        if bytecode.find(placeholder_bytes, index + 1) > -1:
            raise Exception(f'Placeholder for {v} appears more than once!')
        variables[v] = {
            'name': v,
            'type': 'int',
            'index': index,
            'length': len(placeholder_bytes),
        }
    return variables, bytecode, address

        
def encode_varint(number):
    buf = b''
    while True:
        x = number & 0x7f
        number >>= 7
        if number:
            buf += bytes([x | 0x80])
        else:
            buf += bytes([x])
            break
    return buf


def compile_program(filename):
    filename = str(filename)
    teal = open(filename, 'r').read()
    variables, bytecode, address = replace_variables_and_compile(teal)

    with open(filename + '.tok', 'wb') as f:
        f.write(bytecode)

    bytecode_b64 = base64.b64encode(bytecode)
    output = {
        'bytecode': bytecode_b64.decode(),
        'address': address.decode(),
        'size': len(bytecode),
        'variables': [variables[k] for k in sorted(variables.keys())]
    }
    return output


def get_source_url(manifest, filename):
    url = manifest['repo'] +'/tree/' + manifest['ref'] + '/' + filename
    return url


def main(input_filename='asc.manifest.json'):
    manifest = json.load(open(input_filename))
    directory = pathlib.Path(input_filename).parent
    for name, contract in manifest['contracts'].items():
        contract['name'] = name
        for key in ['logic', 'approval_program', 'clear_program']:
            if key in contract:
                filename = contract[key]
                contract[key] = compile_program(directory / filename)
                contract[key]['source'] = get_source_url(manifest, filename)

    with open(directory / 'asc.json', 'w') as f:
        f.write(json.dumps(manifest, indent=2))


if __name__ == '__main__':
    main(*sys.argv[1:])
