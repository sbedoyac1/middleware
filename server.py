from flask import Flask, request
from middleware import middleware,readMessages,deleteline

app = Flask('DemoApp')

# calling our middleware
app.wsgi_app = middleware(app.wsgi_app)

@app.route('/', methods=['GET', 'POST'])
def hello():
    # using 
    user = request.environ['user']
    # return "Hi %s"%user['name']
    fColas = open('colas.txt', 'r')
    colas = fColas.readlines()
    fColas.close()
    subcripciones=[]
    iter=0
    while(iter<len(colas)):
        fSubs = open('suscriptoresMessages' + str(iter) + '.txt', 'r')
        subs = fSubs.readlines()
        if str(user['name']+'\n') in subs:
            subcripciones.append(iter)
        else:
            pass
        iter+=1
    print('Hola %s, Las colas a las que se encuentra subscrito son: \n'%user['name'] )
    for i in subcripciones:
        print('Cola', i)

    consumir = input("Ingrese la cola que desea consumir: ")
    consumo = []
    array = readMessages(int(consumir))
    salir=''
    while(salir!='exit'):
        salir=str(input("Ingrese 'consumir' para consumir de la cola o 'exit' para salir: "))
        if salir=='consumir':
            if array:
                consumo.append(array[0])
                array.pop(0)
                deleteline(int(consumir))    
            else:
                aux = 'No hay mas elementos' 
                array = readMessages(int(consumir))
                salir='exit'
        elif salir!='exit':
            print('Comando no valido')
        else:
            pass
    result='El usuario '+str(user['name'])+' se consumio los siguientes elementos de la cola '+str(consumir)
    count=2
    if consumo:    
        result=result+':\n1.'+str(consumo[0])
        consumo.pop(0)
        for i in consumo:
            result=result+str(count)+'.'+ str(i)
    else:
        result='No había elementos en la cola %s'%consumir

    return result
    

if __name__ == "__main__":
    app.run('127.0.0.1', '5000', debug=True)