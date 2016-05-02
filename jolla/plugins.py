#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import os
from HTTPerror import HTTP404Error
from server import static_setting


def render(filename):
    if static_setting['templates'][-1] != '/':
        static_setting['templates'] = static_setting['templates'] + '/'

    try:
        with open(os.path.abspath(static_setting['templates'] + filename), "r") as f:
            res = f.read()

        return (res, ('Content-Type', 'text/html'))

    except IOError:
        print "<NO SUCH FILE>"
        raise HTTP404Error


def render_json(data):
    if isinstance(data, dict):
        return (json.dumps(data), ('Content-Type', 'application/json'))
    else:
        raise AttributeError


def render_media(filename):
    if static_setting['statics'][-1] != '/':
        static_setting['statics'] = static_setting['statics'] + '/'

    try:
        with open(os.path.abspath(static_setting['statics'] + filename), "r") as f:
            res = f.read()

        if 'css' in filename[-4:]:
            content = ('Content-Type', 'text/css')
        elif 'js' in filename[-4:]:
            content = ('Content-Type', 'application/javascript')
        else:
            raise HTTP404Error
        return (res, content)

    except IOError:
        raise HTTP404Error
