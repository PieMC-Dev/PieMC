import json
import hashlib
import base64
import hmac

mojang_public_key = "MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAE8ELkixyLcwlZryUQcu1TvPOmI2B7vX83ndnWRUaXm74wFfa5f/lwQNTfrLVHa2PmenpGI6JhIMUJaWZrjmMj90NoKNFSNBuKdm8rYiXsfaz3K36x/1U26HpG0ZxK/V1V"

def decode(token):
    header, payload, verify_signature = toke.split(".")
    payload += "=="
    json_data: str = base64.b64decode(payload.replace("-_", "+/").encode())
    return json.loads(json_data)

def encode(header, payload, verify_signature):
    body = []
    body.append(base64.b64encode(json.dumps(header).encode()).decode())
    body.append(base64.b64encode(json.dumps(payload).encode()).decode())
    body.append(base64.b64encode(hmac.new(verifySigniture.encode(), ".".join(body).encode(), hashlib.sha256).hexdigest().upper().encode()).decode())
    return ".".join(body)
