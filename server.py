from flask import Flask, request
from middleware import middleware

app = Flask('DemoApp')

# calling our middleware
app.wsgi_app = middleware(app.wsgi_app)

@app.route('/', methods=['GET', 'POST'])
def hello():
    # using 
    user = request.environ['user']
    # return "Hi %s"%user['name'] 
    
    f3 = open('colas.txt', 'r')
    messages = f3.readlines()
    f3.close()
    print('Las colas disponibles son: \n')
    for i in messages:
        print('Cola', i)

    a = input("Ingrese la cola que desea consumir: ")

    return a
    

if __name__ == "__main__":
    app.run('127.0.0.1', '5000', debug=True)