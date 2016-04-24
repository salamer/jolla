

class buffer(object):

    def __init__(self,value):
        self.data={}

class SessionError(object):
    def __str__(self):
        return "NO SUCH SESSION"

class session(buffer):

    def add_session(self,key,value):
        self.data[key]=value
        return True

    def check_session(self,key,value=None):
        if key in data.keys():
            if value:
                if data[key]==value:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def del_session(self,key):
        if key in data.keys():
            del data[key]
            return True
        else:
            raise SessionError
