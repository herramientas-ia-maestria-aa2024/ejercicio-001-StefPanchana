# file = open("informacion.txt", mode="r")
# if file.readable():
#     print(file.read())
# file.close()

with open("informacion.txt") as archivo:
    firtLine = archivo.readline()
    arrayColumns = firtLine.split(";")
    arrayColumns[3] = arrayColumns[3].replace('\n', "")
    for linea in archivo.readlines():
        array = linea.split(";")
        for (i, valor) in enumerate(array):
            print(arrayColumns[i] + ": " + array[i])
