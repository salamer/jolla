import json


def render(filename):
    with open(filename, "r") as f:
        res = f.read()

    return res

def render_json(data):
    if isinstance(data,dict):
        return json.dumps(data)
    else:
        raise AttributeError
