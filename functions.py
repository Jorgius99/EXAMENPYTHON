def read_data(nombre_fichero):
    data = {}
    with open(nombre_fichero, "r") as file:
        header = file.readline().strip().split(";")
        for line in file:
            values = line.strip().split(";")
            #data[values[0]] = values[1:]
            data={header[i]:values[i] for i in range(len(header)) : values[i] for i in range(len(values))}
    return data


print(read_data("winequality.csv"))