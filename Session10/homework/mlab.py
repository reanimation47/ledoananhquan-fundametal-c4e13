import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds133166.mlab.com:33166/p_t_meeting

host = "ds133166.mlab.com"
port = 33166
db_name = "p_t_meeting"
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
