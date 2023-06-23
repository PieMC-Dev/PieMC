import json
import hashlib
import base64
import hmac

mojang_public_key = "MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAECRXueJeTDqNRRgJi/vlRufByu/2G0i2Ebt6YMar5QX/R0DIIyrJMcUpruK4QveTfJSTp3Shlq4Gk34cD/4GUWwkv0DVuzeuB+tXija7HBxii03NHDbPAD0AKnLr2wdAp"
# old_mojang_public_key = "MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAE8ELkixyLcwlZryUQcu1TvPOmI2B7vX83ndnWRUaXm74wFfa5f/lwQNTfrLVHa2PmenpGI6JhIMUJaWZrjmMj90NoKNFSNBuKdm8rYiXsfaz3K36x/1U26HpG0ZxK/V1V"

def decode(token: str) -> dict:
    header, payload, verifySigniture = token.split(".")
    payload += "=="
    json_data: str = base64.b64decode(payload.replace("-_", "+/").encode())
    return json.loads(json_data)

def encode(header: dict, payload: dict, verifySigniture: str) -> str:
    body: list = []
    body.append(base64.b64encode(json.dumps(header).encode()).decode())
    body.append(base64.b64encode(json.dumps(payload).encode()).decode())
    body.append(base64.b64encode(hmac.new(verifySigniture.encode(), ".".join(body).encode(),
                                          hashlib.sha256).hexdigest().upper().encode()).decode())
    return ".".join(body)
