import json
import os


def render(filename):
    with open(os.path.abspath('templates/' + filename), "r") as f:
        res = f.read()

    return res


def render_json(data):
    if isinstance(data, dict):
        return json.dumps(data)
    else:
        raise AttributeError


def render_media(filename):
    with open(os.path.abspath('statics/' + filename), "r") as f:
        res = f.read()

    return res
