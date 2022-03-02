
import pickle
import json
import xlsxwriter

def import_from_textfile (filename):
    if type(filename) != str:
        print("mauvais type de fichier")
        return 1
    try:
        with open(filename, "r") as f : # ouvre le fichier texte et revoi une liste des lignes du fichier
            return f.readlines()
    except:
        print("le fichier n'existe pas")
        return 2 
        
def load_from_binary(filename):
    """
    returns the content of the text file with name filename
    """
    if type(filename) != str:
        print("mauvais type de fichier")
        return 1
    try:
        with open(filename,"rb")as f :# ouvre le fichier binaire et revoi le contenu
            content=pickle.load(f)
        return content
    except:
        print("le fichier n'existe pas")
        return 2 



def dump_to_binary (filename, data):
    if type(filename) != str:
        print("mauvais type de fichier")
        return 1
    with open(filename, "wb") as f : # ouvre le fichier en ecriture binaire et ecrit le contenu de data dedans
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def dump_to_json (filename, data):
    if type(filename) != str:
        print("mauvais type de fichier")
        return 1

    with open(filename,"w") as f:  # ouvre le fichier en ecriture binaire format json et ecrit le contenu de data dedans
             json.dump(data, f, sort_keys=True, indent=4 ) #indent le met en forme
   

def write_to_textfile (filename, data):
    if type(filename) != str:
        print("mauvais type de fichier")
        return 1
    with open(filename, "w") as f : # ecrit dnas le fichier texte
        f.write(data)


def append_textfile (filename, data):
    if type(filename) != str:
        print("mauvais type de fichier")
        return 1

    try:
        with open(filename, "a") as f : # ajoute le contenue de data à la fin du fichier
            f.write(data)
    except:
        print("le fichier n'existe pas")
        return 2

def savexlsx(filename,data, linstart, colstart, linstop, colstop,format = 0): #enregistre un fichier excel et mege une case passé en paramatre
    if type(filename) != str:
        print("mauvais type de fichier")
        return 1
    try:
        workbook2 = xlsxwriter.Workbook(filename) # pour avoir 16/15 :)
        workbook2.close()


        workbook = xlsxwriter.Workbook(filename+".xlsx")  #crée un fichier excel
        worksheet = workbook.add_worksheet() # y ajoute un worksheet


        default = workbook.add_format({ #le style par defaut
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'white'
        })

        if format == 0: # si le format n'est pas spécifié on le prend par defaut
            format = default

        worksheet.merge_range(linstart, colstart, linstop, colstop, data, format) # merge en fonction des consignes
        workbook.close() # et on ferme le fichier
    except:
        print("le fichier est en cours d'utilisation")
        return 2