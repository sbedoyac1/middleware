from flask import Flask, request
from middleware import middleware

app = Flask('DemoApp')

# calling our middleware
app.wsgi_app = middleware(app.wsgi_app)
#array = ['1','2','3']

@app.route('/', methods=['GET', 'POST'])
def hello():
    # using 
    user = request.environ['user']
    return "Hi %s"%user['name']  
    # user = request.aux
    # aux = array[0]
    # print(array)
    # array.pop(0)
    # print(array)
    # return user
    
    

if __name__ == "__main__":
    app.run('127.0.0.1', '5000', debug=True)