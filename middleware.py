from werkzeug.wrappers import Request, Response, ResponseStream
from os import remove

def credentials():
    f = open ('usuario.txt','r')
    usuarios = f.readlines()
    f.close()
    f1 = open ('contraseña.txt','r')
    contraseñas = f1.readlines()
    f1.close()
    return usuarios,contraseñas

def readMessages(cola):
    f = open ('messages'+str(cola)+'.txt','r')
    messages = f.readlines()
    array = messages
    f.close() 
    return messages


def deleteline(cola):
    a_file = open('messages'+str(cola)+'.txt', 'r')
    lines = a_file.readlines()
    a_file.close()
    del lines[0]
    new_file = open('messages'+str(cola)+'.txt', "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()

    return

class middleware():
    '''
    Simple WSGI middleware
    '''
    # self.userName,self.password = credentials()
    def __init__(self, app):
        self.app = app
        self.userName, self.password = credentials()
        # self.userName = ['pepe','juan']
        # self.password = ['password']

    def __call__(self, environ, start_response):
        request = Request(environ)
        userName = request.authorization['username']
        password = request.authorization['password']
        bandera=0
        j=0
        for i in self.userName:
            if str(i)==str(userName+'\n'):
                if (self.password[j])==password+'\n':
                    bandera=1
                    break
                else:
                    bandera=0
            else:
                bandera=0
            j+=1    
        # these are hardcoded for demonstration
        # verify the username and password from some database or env config variable
        # array = readMessages()
        #print(messages)
        #array = messages
        # print(array)
        if bandera==1:
            aux = userName
            environ['user'] = { 'name': aux }
            return self.app(environ, start_response)       
        # if userName in self.userName:
        #     if password in self.password:                
                # if array:
                #     aux = array[0]
                #     array.pop(0)
                #     deleteline()    
                # else:
                #     aux = 'No hay mas elementos' 
                #     array = readMessages()            
                # environ['user'] = { 'name': aux }
                # return self.app(environ, start_response)
        res = Response(u'Authorization failed', mimetype= 'text/plain', status=401)
        return res(environ, start_response)