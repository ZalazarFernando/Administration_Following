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
            lines = file.readlines()
    except IOError:
        print("Error reading file.")
    finally:
        lines = [line for line in lines if name not in line]

        with open(folder+"/"+category+".txt", "w") as file:
            file.writelines(lines)

#get and set