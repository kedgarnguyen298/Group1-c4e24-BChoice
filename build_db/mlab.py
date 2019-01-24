# mongodb://<dbuser>:<dbpassword>@ds225010.mlab.com:25010/foody
import mongoengine

host = "ds225010.mlab.com"
port = 25010
db_name = "foody"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())