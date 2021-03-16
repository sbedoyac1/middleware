from werkzeug.wrappers import Request, Response, ResponseStream
from os import remove

def readMessages():
    f = open ('messages.txt','r')
    messages = f.readlines()
    array = messages
    print(messages)
    f.close()
    
    return messages


def deleteline():
    a_file = open("messages.txt", "r")
    lines = a_file.readlines()
    a_file.close()
    del lines[0]
    new_file = open("messages.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()

    return

class middleware():
    '''
    Simple WSGI middleware
    '''

    def __init__(self, app):
        self.app = app
        self.userName = ['pepe','juan']
        self.password = ['password']

    def __call__(self, environ, start_response):
        request = Request(environ)
        userName = request.authorization['username']
        password = request.authorization['password']
        
        # these are hardcoded for demonstration
        # verify the username and password from some database or env config variable
        array = readMessages()
        #print(messages)
        #array = messages
        print(array)
        if userName in self.userName:
            if password in self.password:                
                if array:
                    aux = array[0]
                    array.pop(0)
                    deleteline()    
                else:
                    aux = 'No hay mas elementos' 
                    array = readMessages()            
                environ['user'] = { 'name': aux }   
                return self.app(environ, start_response)
            
        

        res = Response(u'Authorization failed', mimetype= 'text/plain', status=401)
        return res(environ, start_response)