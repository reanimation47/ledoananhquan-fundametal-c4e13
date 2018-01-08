import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds129796.mlab.com:29796/oldstuff

host = "ds129796.mlab.com"
port = 29796
db_name = "oldstuff"
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
