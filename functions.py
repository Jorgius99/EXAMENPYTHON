def read_data(nombre_fichero):
    data = {}
    with open(nombre_fichero, "r") as file:
        header = file.readline().strip().split(";")
        for line in file:
            values = line.strip().split(";")
            data[values[0]] = values[1:]   
    return data


#print(read_data("winequality.csv"))


import csv
with open('winequality.csv', 'r') as file:
    reader = csv.reader(file)
    header = file.readline().strip().split(";")
    for row in reader:
        print({header[i]: row[i] for i in range(len(header))})