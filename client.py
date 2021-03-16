def fillArray():
    message= str(input("Enter message: "))
    print(message)
    f = open ('messages.txt','a')
    f.write(message+'\n')
    f.close()

if __name__ == "__main__":
    fillArray()