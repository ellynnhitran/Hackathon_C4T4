# mongodb://<dbuser>:<dbpassword>@ds125872.mlab.com:25872/hackathon_c4t4

import mongoengine

host = "ds125872.mlab.com"
port = 25872
db_name = "hackathon_c4t4"
user_name = "hackathon"
password = "codethechange123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())