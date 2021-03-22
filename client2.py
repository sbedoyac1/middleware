def createUsers():
    option = input("Ingrese o registrese: ")
    if option=='registrar':
        username= str(input("Ingrese el username a registrar: "))
        fRead = open('usuario.txt', 'r')
        usuarios = fRead.readlines()
        fRead.close()
        for i in usuarios:
            if((username+'\n')==i):
                print('El ususario ya existe, cree uno diferente')
                exit()

        f = open('usuario.txt', 'a')
        f.write(username+'\n')
        f.close()    
        
        password= str(input("Ingrese la contraseña: "))
        f2 = open('contraseña.txt', 'a')
        f2.write(password+'\n')
        f2.close()
        
        f3 = open('colas.txt', 'r')
        messages = f3.readlines()
        f3.close()
        print('Las colas disponibles son: \n')
        for i in messages:
            print('Cola', i)
        cola = ''
        aux=[]
        while (cola != 'exit'):
            cola = str(input("Ingrese las cola a la que se quiere susbcribir (escriba exit para salir): "))
            aux.append(cola)
            f = open('suscriptoresMessages'+ cola + '.txt', 'a')
            f4 = open('suscriptoresMessages'+ cola + '.txt', 'r')
            messages = f4.readlines()
            f4.close()
            if username in messages:
                print(username)
                print("Ya se encuentra suscrito a la cola")
            else:
                print('Ususario suscrito a la cola ', cola)
                if(cola != 'exit'):
                    f.write(username)
        print(aux)           
        aux.pop(len(aux)-1)
        print(aux)
        res = [] 
        for i in aux: 
            if i not in res: 
                res.append(i)
        print(res)
        for i in res:
            f = open('suscriptoresMessages'+ i + '.txt', 'a')
            f.write('\n')
            f.close()
    elif(option=='ingrese'):
        username= str(input("Ingrese el usuario: "))
        username = username + '\n'
        fRead = open('usuario.txt', 'r')
        usuarios = fRead.readlines()
        fRead.close()
        pos=0
        aux=-1
        for i in usuarios:
            if i!=username:
                pos+=1
            else:
                # pos+=1
                print(pos)
                aux=pos

        if aux==-1:
            print("El usuario no existe, cree un usuario nuevo")
            exit()
                
        password= str(input("Ingrese la contraseña: "))
        fRead = open('contraseña.txt', 'r')
        contraseña = fRead.readlines()
        fRead.close()
        print(contraseña)
        if((password+'\n')==contraseña[aux]):
            print("Contraseña correcta")
            
            f3 = open('colas.txt', 'r')
            messages = f3.readlines()
            f3.close()
            print('Las colas disponibles son: \n')
            for i in messages:
                print('Cola', i)
            cola = ''
            aux=[]
            while (cola != 'exit'):
                cola = str(input("Ingrese las cola a la que se quiere susbcribir (escriba exit para salir): "))
                aux.append(cola)
                f = open('suscriptoresMessages'+ cola + '.txt', 'a')
                f4 = open('suscriptoresMessages'+ cola + '.txt', 'r')
                messages = f4.readlines()
                f4.close()
                if username in messages:
                    print(username)
                    print("Ya se encuentra suscrito a la cola")
                else:
                    print('Ususario suscrito a la cola ', cola)
                    if(cola != 'exit'):
                        f.write(username)

        else:
            print("Contraseña incorrecta")
            exit()

    else:
        print("Opcion no reconocida")
    

if __name__ == "__main__":
    createUsers()