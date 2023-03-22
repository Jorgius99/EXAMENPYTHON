def read_data(nombre_fichero):
    data = {}
    with open(nombre_fichero, "r") as file:
        header = file.readline().strip().split(";")
        for column in header:
            data[column] = []
        for line in file:
            values = line.strip().split(";")
            for i in range(len(values)):
                data[header[i]].append(values[i])
    return data

print(read_data("winequality.csv"))
