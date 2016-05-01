#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import os
from plugins import HTTP404Error



def render(filename):
    try:
        with open(os.path.abspath('templates/' + filename), "r") as f:
            res = f.read()

        return (res, ('Content-Type', 'text/html'))
    except IOError:
        print "NO SUCH FILE"
        raise HTTP404Error


def render_json(data):
    if isinstance(data, dict):
        return (json.dumps(data), ('Content-Type', 'application/json'))
    else:
        raise AttributeError


def render_media(filename):
    with open(os.path.abspath('statics/' + filename), "r") as f:
        res = f.read()

    return res
