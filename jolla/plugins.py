#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import os


def render(filename):
    with open(os.path.abspath('templates/' + filename), "r") as f:
        res = f.read()

    return (res, ('Content-Type', 'text/html'))


def render_json(data):
    if isinstance(data, dict):
        return (json.dumps(data), ('Content-Type', 'application/json'))
    else:
        raise AttributeError


def render_media(filename):
    with open(os.path.abspath('statics/' + filename), "r") as f:
        res = f.read()

    return res
