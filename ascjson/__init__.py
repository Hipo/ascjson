import json
from algosdk.future.transaction import LogicSig, StateSchema

from .read import get_program_bytes


class ASCJSON:
    def __init__(self, fp=None, s=None, data=None) -> None:
        if fp:
            self.data = json.load(fp)
        elif s:
            self.data = json.loads(s)
        elif data:
            self.data = dict(data)

    def get_definition(self, name):
        definition = self.data['contracts'][name]
        return definition

    def get_program_bytes(self, program_definition, variables=None):
        return get_program_bytes(program_definition, variables)
    
    def get_logicsig(self, name, variables=None):
        definition = self.get_definition(name)
        program_bytes = self.get_program_bytes(definition['logic'], variables)
        return LogicSig(program=program_bytes)

    def get_app(self, name, variables=None):
        definition = self.get_definition(name)
        approval_program_bytes = self.get_program_bytes(definition['approval_program'], variables)
        clear_program_bytes = self.get_program_bytes(definition['clear_program'], variables)
        app = App(
            approval_program=approval_program_bytes,
            clear_program=clear_program_bytes,
            global_state_schema=StateSchema(**definition['global_state_schema']),
            local_state_schema=StateSchema(**definition['local_state_schema']),
        )
        return app


class App:
    def __init__(self, approval_program: bytes, clear_program: bytes, global_state_schema: StateSchema, local_state_schema: StateSchema) -> None:
        self.approval_program = approval_program
        self.clear_program = clear_program
        self.global_state_schema = global_state_schema
        self.local_state_schema = local_state_schema
