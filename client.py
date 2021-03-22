def fillArray():
    message= str(input("Ingrese la opcion:\n (Opción 'create': para crear una cola)\n (Opción 'add': para añadir elementos a una cola)\n"))
    print(message)
    if(message=='create'):
        f = open('colas.txt', 'r')
        messages = f.readlines()
        if (messages):
            print(messages[-1])
            iter = int(messages[-1]) + 1
            print (iter)
        else:
            f3 = open('colas.txt', 'a')
            f3.write('0'+'\n')
            f3.close()
            iter = 0

        f2 = open('messages' + str(iter) + '.txt', 'a')
        f4 = open('suscriptoresMessages'+ str(iter) + '.txt', 'a')
        f4.close()
        while(message!='exit'):
            message= str(input("Ingrese el mensaje o exit para salir:"))
            if(message != 'exit'):
                f2.write(message+'\n')
        if(iter != 0):    
            f3 = open('colas.txt', 'a')
            f3.write(str(iter)+'\n')
        f.close()
        f2.close()
        f3.close()
        
    elif (message == 'add'):
        try:
            f = open('colas.txt', 'r')
            messages = f.readlines()
            print('Las colas disponibles son: \n')
            for i in messages:
                print('Cola', i)
            cola = str(input("Ingrese el numero de la cola a la que va a agegar elementos:"))
            f2 = open('messages' + str(cola) + '.txt', 'a')
            print('Escribiendo sobre cola ',cola)
            while(message!='exit'):
                message= str(input("Ingrese el mensaje o exit para salir:"))
                if(message != 'exit'):
                    f2.write(message+'\n')
        except:
            print("Error añadiendo el elemento")    
    else:
        print('Error')

if __name__ == "__main__":
    fillArray()