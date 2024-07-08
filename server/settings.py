import os

os.environ["TZ"] = "America/Sao_Paulo"
os.environ["PROFILE_TABLE"] = "profile"
os.environ["AWS_DYNAMO_DB_ENDPOINT"] = "http://localhost:8000"
class Config(object):
    DEBUG = True
    TESTING = True
    JSON_AS_ASCII = False