#!/usr/bin/env python
# -*- coding: utf-8 -*-


class buffer(object):

    def __init__(self):
        self._data = {}


class SessionError(Exception):

    def __str__(self):
        return "<NO SUCH SESSION>"


class session(buffer):

    def __str__(self):
        return "Jolla.jolla_sessionObject"

    def __repr__(self):
        return "<class 'jolla_sessionObject'>"

    def empty(self):
        if not self._data:
            return True
        else:
            return False

    def session_count(self):
        return len(self._data)

    def add_value(self, key, value):
        self._data[key] = value
        return True

    def check_value(self, key, value=None):
        if key in self._data.keys():
            if value:
                if self._data[key] == value:
                    return True

                else:
                    return False
            else:
                return True

        else:
            return False

    def del_value(self, key):
        if key in self._data.keys():
            del self._data[key]
            return True
        else:
            raise SessionError

    def get_value(self, key):
        if key in self._data.keys():
            return self._data[key]
        else:
            raise SessionError
