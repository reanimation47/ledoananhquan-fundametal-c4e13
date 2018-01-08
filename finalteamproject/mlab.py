import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds163836.mlab.com:63836/user_base

host = "ds163836.mlab.com"
port = 63836
db_name = "user_base"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
