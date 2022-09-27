# ASCJSON
Package Algorand contract bytecode and metadata in standard format for easier consumption by clients.


## Usage example

### Define `asc.manifest.json`
The following `asc.manifest.json` was defined for Tinyman V1.
```json
{
    "repo": "https://github.com/tinymanorg/tinyman-contracts-v1",
    "ref": "13acadd1a619d0fcafadd6f6c489a906bf347484",
    "contracts": {
        "pool_logicsig": {
            "type": "logicsig",
            "logic": "contracts/pool_logicsig.teal.tmpl"
        },
        "validator_app": {
            "type": "app",
            "approval_program": "contracts/validator_approval.teal",
            "clear_program": "contracts/validator_clear_state.teal",
            "global_state_schema": {
                "num_uints": 0,
                "num_byte_slices": 0
            },
            "local_state_schema": {
                "num_uints": 16,
                "num_byte_slices": 0
            }
        }
    }
}
```

### Build `asc.manifest.json` -> `asc.json`
```bash
python ascjson.build tinyman-contracts-v1/asc.manifest.json
```

This produces `tinyman-contracts-v1/asc.json`:

```json
{
  "repo": "https://github.com/tinymanorg/tinyman-contracts-v1",
  "ref": "13acadd1a619d0fcafadd6f6c489a906bf347484",
  "contracts": {
    "pool_logicsig": {
      "type": "logicsig",
      "logic": {
        "bytecode": "BCAIAQCBgICAgICAgPABgICAgICAgIDwAQMEBQYlJA1EMQkyAxJEMRUyAxJEMSAyAxJEMgQiDUQzAQAxABJEMwEQIQcSRDMBGIGCgICAgICAgPABEkQzARkiEjMBGyEEEhA3ARoAgAlib290c3RyYXASEEAAXDMBGSMSRDMBG4ECEjcBGgCABHN3YXASEEACOzMBGyISRDcBGgCABG1pbnQSQAE7NwEaAIAEYnVybhJAAZg3ARoAgAZyZWRlZW0SQAJbNwEaAIAEZmVlcxJAAnkAIQYhBSQjEk0yBBJENwEaARclEjcBGgIXJBIQRDMCADEAEkQzAhAhBBJEMwIhIxJEMwIiIxwSRDMCIyEHEkQzAiQjEkQzAiWACFRNUE9PTDExEkQzAiZRAA+AD1RpbnltYW5Qb29sMS4xIBJEMwIngBNodHRwczovL3RpbnltYW4ub3JnEkQzAikyAxJEMwIqMgMSRDMCKzIDEkQzAiwyAxJEMwMAMQASRDMDECEFEkQzAxElEkQzAxQxABJEMwMSIxJEJCMTQAAQMwEBMwIBCDMDAQg1AUIBsTMEADEAEkQzBBAhBRJEMwQRJBJEMwQUMQASRDMEEiMSRDMBATMCAQgzAwEIMwQBCDUBQgF8MgQhBhJENwEcATEAE0Q3ARwBMwQUEkQzAgAxABNEMwIUMQASRDMDADMCABJEMwIRJRJEMwMUMwMHMwMQIhJNMQASRDMDESMzAxAiEk0kEkQzBAAxABJEMwQUMwIAEkQzAQEzBAEINQFCAREyBCEGEkQ3ARwBMQATRDcBHAEzAhQSRDMDFDMDBzMDECISTTcBHAESRDMCADEAEkQzAhQzBAASRDMCESUSRDMDADEAEkQzAxQzAwczAxAiEk0zBAASRDMDESMzAxAiEk0kEkQzBAAxABNEMwQUMQASRDMBATMCAQgzAwEINQFCAJAyBCEFEkQ3ARwBMQATRDMCADcBHAESRDMCADEAE0QzAwAxABJEMwIUMwIHMwIQIhJNMQASRDMDFDMDBzMDECISTTMCABJEMwEBMwMBCDUBQgA+MgQhBBJENwEcATEAE0QzAhQzAgczAhAiEk03ARwBEkQzAQEzAgEINQFCABIyBCEEEkQzAQEzAgEINQFCAAAzAAAxABNEMwAHMQASRDMACDQBD0M=",
        "address": "ABUKAXTANWR6K6ZYV75DWJEPVWWOU6SFUVRI6QHO44E4SIDLHBTD2CZ64A",
        "size": 881,
        "variables": [
          {
            "name": "TMPL_ASSET_ID_1",
            "type": "int",
            "index": 15,
            "length": 10
          },
          {
            "name": "TMPL_ASSET_ID_2",
            "type": "int",
            "index": 5,
            "length": 10
          },
          {
            "name": "TMPL_VALIDATOR_APP_ID",
            "type": "int",
            "index": 74,
            "length": 10
          }
        ],
        "source": "https://github.com/tinymanorg/tinyman-contracts-v1/tree/13acadd1a619d0fcafadd6f6c489a906bf347484/contracts/pool_logicsig.teal.tmpl"
      },
      "name": "pool_logicsig"
    },
    "validator_app": {
      "type": "app",
      "approval_program": {
        "bytecode": "BCAHAAHoB+UHBf///////////wHAhD0mDQFvAWUBcAJhMQJhMgJsdARzd2FwBG1pbnQBdAJjMQJwMQJjMgJwMjEZgQQSMRkhBBIRMRmBAhIRQATxMRkjEjEbIhIQQATjNhoAgAZjcmVhdGUSQATUMRkjEjYaAIAJYm9vdHN0cmFwEhBAA/MzAhIzAggINTQiK2I1ZSI0ZXAARDUBIicEYjVmNGZAABEiYCJ4CTEBCDMACAk1AkIACCI0ZnAARDUCIicFYjVnKDRlFlA1byI0b2I1PSg0ZhZQNXAiNHBiNT4oNGcWUDVxIjRxYjU/IipiNUA0ATQ9CTVHNAI0Pgk1SDEAKVA0ZRZQNXkxAClQNGYWUDV6MQApUDRnFlA1ezYaAIAGcmVkZWVtEkAAWjYaAIAEZmVlcxJAABw2GgAnBhI2GgAnBxIRNhoAgARidXJuEhFAAG0ANGdJRDMCERJEMwISRDMCFDIJEkQ0PzMCEgk1PzRAMwISCTVAIio0QGYiNHE0P2YjQzMCFDMCBzMCECMSTTYcARJENDREIigzAhEWUEpiNDQJZiMxAClQMwIRFlBKYjQ0CUlBAANmI0NIaCNDMgciJwhiCUk1+kEARiInCWIiJwpiNPodTEAANx4hBSMeHzX7SEhIIicLYiInDGI0+h1MQAAdHiEFIx4fNfxISEgiJwk0+2YiJws0/GYiJwgyB2YzAxIzAwgINTU2HAExABNENGdBACIiNGdwAEQ1BiIcNAYJND8INQQ2GgAnBhJAASA0ZzMEERJENhoAJwcSQABVNhwBMwQAEkQzBBI0Rx00BCMdH0hITEhJNRA0NAk1yTMEEjRIHTQEIx0fSEhMSEk1ETQ1CTXKNBA0ERBENEc0EAk1UTRINBEJNVI0BDMEEgk1U0ICCjYcATMCABJENEc0NAg1UTRINDUINVI0BCISQAAuNDQ0BB00RyMdH0hITEg0NTQEHTRIIx0fSEhMSEoNTUk0BAg1UzMEEgk1y0IBvyInBTMEEUk1Z2YoNGcWUDVxIjRncABERDRnNGUTRDRnNGYTRDMEEiQISR018DQ0NDUdNfFKDEAACBJENPA08Q5EMwQSJAgjCEkdNfA0NDQ1HTXxSg1AAAgSRDTwNPENRCQ1PzQEMwQSJAgINVNCAU82HAEzAgASRDMCETRlEjMDETRmEhBJNWRAABkzAhE0ZhIzAxE0ZRIQRDRINRI0RzUTQgAINEc1EjRINRM2GgGAAmZpEkAAWjYaAYACZm8SRDQ1JAs0Eh00EzQ1CSUdH0hITEgjCEk1FSINNDU0EwwQRDQ0NBUJNGRBABM1yTRHNBUINVE0SDQ1CTVSQgBnNco0SDQVCDVSNEc0NQk1UUIAVDQ0STUVJQs0Ex00EiQLNDQlCx4fSEhMSEk1FCINNBQ0EwwQRDQUNDUJNGRBABM1yjRHNDQINVE0SDQUCTVSQgATNck0RzQUCTVRNEg0NAg1UkIAADQVIQQLNAQdgaCcATQSHR9ISExISTUqNAQINVNCADsiKzYaARdJNWVmIicENhoCF0k1ZmY0ZXEDRIABLVCABEFMR080ZkEABkg0ZnEDRFAzAiZJFYEPTFISQyIqNEA0KghmIjRxND80Kgg0ywhmIjRvND00yQhmIjRwND40yghmIoACczE0UWYigAJzMjRSZiInCjRSIQYdNFEjHR9ISExIZiInDDRRIQYdNFIjHR9ISExIZiKAA2lsdDRTZjTLQQAJIzR7SmI0ywhmNMlBAAkjNHlKYjTJCGY0ykEACSM0ekpiNMoIZiNDI0MiQw==",
        "address": "BUQHXHPLMYUVS3P2INJ2EUJFCSNT6LNUGXVM6T2SZ27TDRDYLUMWCFYW3E",
        "size": 1351,
        "variables": [],
        "source": "https://github.com/tinymanorg/tinyman-contracts-v1/tree/13acadd1a619d0fcafadd6f6c489a906bf347484/contracts/validator_approval.teal"
      },
      "clear_program": {
        "bytecode": "BIEB",
        "address": "P7GEWDXXW5IONRW6XRIRVPJCT2XXEQGOBGG65VJPBUOYZEJCBZWTPHS3VQ",
        "size": 3,
        "variables": [],
        "source": "https://github.com/tinymanorg/tinyman-contracts-v1/tree/13acadd1a619d0fcafadd6f6c489a906bf347484/contracts/validator_clear_state.teal"
      },
      "global_state_schema": {
        "num_uints": 0,
        "num_byte_slices": 0
      },
      "local_state_schema": {
        "num_uints": 16,
        "num_byte_slices": 0
      },
      "name": "validator_app"
    }
  }
}
```


### Read `asc.json`


```python
import ascjson
from algosdk.future import transaction

asc = ascjson.ASCJSON(open('asc.json'))

# Creating the app on chain using the app definition
app = asc.get_app('validator_app')

txn = transaction.ApplicationCreateTxn(
    sender=APP_CREATOR_ADDRESS,
    sp=sp,
    approval_program=app.approval_program,
    clear_program=app.clear_program,
    global_schema=app.global_schema,
    local_schema=pp.local_schema,
)

# Using a LogicSig with template variables
logicsig = asc.get_logicsig('pool_logicsig', dict(asset_id_2=0, asset_id_1=1, validator_app_id=3))
print(logicsig.address())
```
