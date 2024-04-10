file = open("informacion.txt", mode="r")
if file.readable():
    print(file.read())
file.close()