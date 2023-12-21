import os


def save_element(folder, category, name, specification):
    try:
        with open("apps/"+folder+"/"+category+".txt", 'a') as file:
            file.write(name+" - "+specification+"\n")
    except IOError:
        print("Error al guardar los datos en el archivo")

def compare_with_file(folder, category, name):
    try:
        with open("apps/"+folder+"/"+category+".txt", 'r') as file:
            line = file.readline()

            if name in line:
                return 1
    except IOError:
        print("Error al guardar los datos en el archivo")

    return 0

#conectado, aun no verificado
def delete_name(folder, category, name):
    try:
        with open("apps/"+folder+"/"+category+".txt", "r") as file:
            lines = file.readlines()
    except IOError:
        print("Error reading file.")
        return

    with open("apps/"+folder+"/"+category+".txt", "w") as file:
        for line in lines:
            if name not in line:
                file.write(line)

#get and set
def get_app_available():
    apps_folder = os.path.join(os.path.dirname(__file__), "apps")

    try:
        app_folders = [folder for folder in os.listdir(apps_folder) if os.path.isdir(os.path.join(apps_folder, folder))]
        return app_folders
    except IOError:
        print("Error al obtener las carpetas de la carpeta 'apps'")
        return []
    
def get_categories_available(folder):
    folder_path = os.path.join(os.path.dirname(__file__), "apps", folder)

    try:
        txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt") and os.path.isfile(os.path.join(folder_path, file))]
        return txt_files
    except IOError:
        print(f"Error al obtener los archivos .txt de la carpeta '{folder}'")
        return []