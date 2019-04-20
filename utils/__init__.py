import hashlib

def hash256(value):
    return hashlib.sha256(value.encode()).hexdigest()
