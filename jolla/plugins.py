#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import os
from HTTPerror import HTTP404Error, HTTP302Error
from server import static_setting
import logging


class HeaderError(Exception):

    def __init__(self):
        pass


class HeaderTupleError(HeaderError):

    def __init__(self):
        logging.debug("<the header must be two tuples>")
        HeaderError.__init__()


def render(filename, extra_header=None):
    if static_setting['templates'][-1] != '/':
        static_setting['templates'] = static_setting['templates'] + '/'

    try:
        with open(os.path.abspath(static_setting['templates'] + filename), "r") as f:
            res = f.read()

        if not extra_header:
            return (res, [('Content-Type', 'text/html')])
        else:
            if isinstance(extra_header, tuple):
                if len(extra_header) == 2:
                    extra_header = [
                        ('Content-Type', 'text/html'), extra_header]
                    return (res, extra_header)
                else:
                    raise HeaderTupleError
            elif isinstance(extra_header, list):
                for header in extra_header:
                    if len(header) != 2:
                        raise HeaderTupleError
                extra_header.append(('Content-Type', 'text/html'))
                return (res, extra_header)
            else:
                raise HeaderTupleError

    except IOError:
        logging.warning("<NO FILE %s>" % filename)
        raise HTTP404Error


def render_json(data, extra_header=None, indent=0):
    if not extra_header:
        return (json.dumps(data, ensure_ascii=False, indent=indent), [('Content-Type', 'application/json')])
    else:
        if isinstance(extra_header, tuple):
            if len(extra_header) == 2:
                extra_header = [
                    ('Content-Type', 'text/html'), extra_header]
                return (json.dumps(data, ensure_ascii=False, indent=indent), extra_header)
            else:
                raise HeaderTupleError
        elif isinstance(extra_header, list):
            for header in extra_header:
                if len(header) != 2:
                    raise HeaderTupleError
            extra_header.append(('Content-Type', 'text/html'))
            return (json.dumps(data, ensure_ascii=False, indent=indent), extra_header)
        else:
            raise HeaderTupleError


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


def redirect(path):

    raise HTTP302Error(path)
