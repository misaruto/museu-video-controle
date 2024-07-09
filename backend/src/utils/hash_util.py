import os
import hashlib

def generate_sha512_hash(data):
    sha512 = hashlib.sha512()
    sha512.update(data.encode('utf-8'))
    return sha512.hexdigest()

def generate_sha256_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8')) 
    return sha256.hexdigest()

def validate_fixed_token(client_token):
    not_randon_secret_key = os.getenv("SERVER_SECRET_KEY")
    return generate_sha256_hash(generate_sha512_hash(client_token) + generate_sha512_hash(not_randon_secret_key) + generate_sha256_hash(client_token)) == os.getenv("SERVER_SECRET_TOKEN")
