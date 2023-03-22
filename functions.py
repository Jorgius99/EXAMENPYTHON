import csv
def read_data(nombre_fichero):
    data = {}
    with open(nombre_fichero, "r") as file:
        header = file.readline().strip().split(";")
        for line in file:
            values = line.strip().split(";")
            data[values[0]] = values[1:]   
    return data


print(read_data("winequality.csv"))
