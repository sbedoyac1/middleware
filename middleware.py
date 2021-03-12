from werkzeug.wrappers import Request, Response, ResponseStream

class middleware():
    '''
    Simple WSGI middleware
    '''

    def __init__(self, app):
        self.app = app
        self.userName = ['pepe','juan']
        self.password = 'IamIronMan'
        self.tipo = ['cola','canal']

    def __call__(self, environ, start_response):
        request = Request(environ)
        userName = request.authorization['username']
        password = request.authorization['password']
        #tipo = request.authorization['tipo']
        
        # these are hardcoded for demonstration
        # verify the username and password from some database or env config variable
                
        if userName in self.userName:
            if password == self.password:
                environ['user'] = { 'name': ['cola','canal'] , 'hello' : 'canal'}
                return self.app(environ, start_response)

        res = Response(u'Authorization failed', mimetype= 'text/plain', status=401)
        return res(environ, start_response)