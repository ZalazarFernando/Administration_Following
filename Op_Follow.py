def save(folder, category, name, specification):
    try:
        with open(folder+"/"+category+".txt", 'a') as file:
            file.write(name+" - "+specification+"\n")
    except IOError:
        print("Error al guardar los datos en el archivo")

def compare_with_file(folder, category, name):
    try:
        with open(folder+"/"+category+".txt", 'r') as file:
            line = file.readline()

            if name in line:
                return 1
    except IOError:
        print("Error al guardar los datos en el archivo")

    return 0

#conectado, aun no verificado
def delete_name(folder, category, name):
    lines = []
    try:
        with open(folder+"/"+category+".txt", "r") as file:
            lines.append(file.readline())
    except IOError:
        print("error")
    finally:
        for line in lines:
            if name in line:
                lines.remove(line)

        with open(folder+"/"+category+".txt", "a") as file:
            file.write(lines)
