import random
import pickle
import xlsxwriter
import json
import tools


######### Liste de fichier exploité/produit ####################################################
#   tools : module agissant sur les fichiers
#   PPCandidate : module qui s'occupe des emploi du temps
#   Run/test_PPcandiate : lance le programme qui s'occupe de trouver le meilleur
#   heure : nombre d'heure à caser dans une semaine
#   needs.pickle remplacé par heure
#   
#   
#   
#   semester 1-1 : fichier Excel ou est enregistrer le meilleur emploi du temps produit
#   semester 1-2 : fichier Excel ou est enregistrer le deuxieme meilleur emploi du temps produit
#   save_best_emp.json : enregistre le meilleur emploi du temps au format json
#   save_best_emp.pickle : enregistre le meilleur emploi du temps au format pickle
#   ouverture : fichier de test comparant l'original et la sauvgarde
#
##############################################################################


class Candidate:
    """
    Candidate class
    ____________________________________________________________________________
    FIELDS
    private field : plannings
        list of four lists, each one devided as a list of 10 empty lists
    ____________________________________________________________________________
    METHODS
    public __init__() : creates the field plannings
    public add_course() : adds a given course to the planning p (0..3) at the
        idx position (0..9)
    public get_course() sert a rien mais vu qu'il y est mieux vaut ne pas l'oublier :)
    public get_content() : returns a copy of the field plannings (for display)
    public disp_schedules() : prints each semester content in the console
    public save_schedules(filename) : saves schedules in a pickle file
    public write_xlsx(filename) : saves schedules in an excel file
    """

    def __init__(self): #constructeur de la class

        self.__s1 = [[] for x in range(10)]
        self.__s2 = [[] for x in range(10)]
        self.__s3 = [[] for x in range(10)]
        self.__s4 = [[] for x in range(10)]
        self.__plannings = [self.__s1,self.__s2,self.__s3,self.__s4]
        

    
    def add_course(self, course, p, idx):

        #print(self.__plannings[p][idx])
        if idx > 9: #si l'index est supérieur à 9
            return 1
        if p > 3: # si le semestre est supérieur à 3
            return 2
        if type(course) != dict: #si le cours n'est pas un dictionnaire
            return 3
    
        a = [] #liste vide
        a.append(course)
        self.__plannings[p][idx].append(a)
        self.__plannings[p][idx][0].append(course) #ajoute le cours avec un degré en plus
       
      

    def efface(self): # remise à zero. l'appel du contructeur est potentiellemnt aussi possible ?
        self.__s1 = [[],[],[],[],[],[],[],[],[],[]]
        self.__s2 = [[],[],[],[],[],[],[],[],[],[]]
        self.__s3 = [[],[],[],[],[],[],[],[],[],[]]
        self.__s4 = [[],[],[],[],[],[],[],[],[],[]]
        self.__plannings = [self.__s1,self.__s2,self.__s3,self.__s4]

   
    def get_course(self): #renvoi le planning
        
        return self.__plannings
        

    def get_content(self):#revoi le planning
        """
        returns the content of the schedules
        """
        return self.__plannings # renvoi le planning privé
        

    def disp_schedules(self): #affiche le planning
       
        print("affiche le programme")
        
        print("Semester 1 :",self.__plannings[0])# affiche le contenue des semstres
        print("Semester 2 :",self.__plannings[1])
        print("Semester 3 :",self.__plannings[2])
        print("Semester 4 :",self.__plannings[3])
        

    def save_schedules(self, filename,emp =0): #enregiste le planning en PICKLE et en JSON parce que cest mieux.
        """
        saves the content of the object Candidate in a pickle file
        displays
        "[INFO] candidate saved"
        in the console once done
        """
        if emp == 0:
            emp = self.__plannings

        tools.dump_to_binary(filename +".pickle", emp)
        tools.dump_to_binary(filename , emp)
        
        tools.dump_to_json(filename +".json", emp)
        return print("done")



    ######## Fonction de cout de l'emploi du temps ########

    def cost(self,emp = 0):
        
        if emp == 0: # si aucun emploi du temps n'est spécifié prend celui de la class
            emp = self.__plannings
        

        cost = 0

        for i in range(0,10,2):# FONCTION de COUT testant touts les matins

            c = 0 #compteur
            ca = 0# compteur
            ca2 = 0# compteuer
            
            try:    
                for j in range(len(emp[0][i][0])):#pour chaque cours dans une demi journée
                    try:
                        if emp[0][i][0][j]["contrainte"] != -1: #si contrainte = -1 alors pas de contriante sinon si c'est le mauvais jour on sevit avec un haut cout.
                            if emp[0][i][0][j]["contrainte"] != i:
                                cost +=1000 #100 est énorme pour etre sur de l'eliminer
                
                    
                            c += int(emp[0][i][0][j]["duration"]) # compte la duree de cours par demi journee matin
                            ca += int(emp[0][i][0][j]["duration"]) # compte la dureee de cours par jour
                    except:
                        pass
            except:
                pass
            try:

                for j in range(len(emp[0][i+1][0])):# de meme.
                    if emp[0][i+1][0][j]["contrainte"] != -1:
                        if emp[0][i+1][0][j]["contrainte"] != i+1:
                            cost +=1000 # de meme pour l'apres midi 
                    ca2 +=emp[0][i+1][0][j]["duration"]
                 
                    ca += emp[0][i+1][0][j]["duration"]
            except:
                pass
            if c != 4:#pas 4 cours le matin le cout augmente
                cost += 50
            if c > 4:# plus de 4 cours le matin de meme
                cost += c-1
        
            if ca >7:# plus de 7 heure de cours par jour
                cost +=6
            if ca2 >6:# plus de 7 heure de cours par apres midi
                cost +=1000 
            if ca2 >6:
                cost +=10
        return cost # on renvoi le cout de l'emploi du temps totale
    
        


    def write_xlsx(self, filename,planning = 0):
        """
        write the content of the Candidate object into an excel file
        this function must
        + define one cell formating per course
        + evaluate how many cells should be merged for optimal schedule reading
        + place the courses at the corresponding place
        The most suitable function of the xlsxwriter package is called
        merge_range(first_lin, first_col, last_lin, last_col, text, fromat)
        for more information :
        https://xlsxwriter.readthedocs.io/worksheet.html#merge_range
        """

        if planning == 0:
            planning = self.__plannings
        #pour pouvoir utiliser la fonction d'ecriture excel avec nomporte quelle emploi du temps.
        


        #ouverture du fichier et création du worksheet
        workbook = xlsxwriter.Workbook(filename+".xlsx")
        worksheet = workbook.add_worksheet("semester 1 ")
      
        #gestion de la taille des lignes 
        for i in range(0,15):
            worksheet.set_row(i, 25) 
        
        # Some data we want to write to the worksheet.
        merge_formatt = workbook.add_format({'bold': 1,'border': 1,'align': 'center','valign': 'vcenter','fg_color': 'yellow'})
        
        row = 1
        col = 0
        h =8
        
        cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1,'fg_color': 'white'}) 
        for i in range(0,13):
            
            t = str(h) +"h - "+ str(h+1) + "h"
            worksheet.write(row,col,t,cell_format)
            row+=1
            h +=1
        
        row = 0 #ligne excel
        col = 1 # colone excel
        

        cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1,'fg_color': 'white','text_wrap': True}) 


        ######## Ajout en-tete emplois du temps #######
        worksheet.merge_range(row,col, row,col +3,"lundi" , cell_format) 
        worksheet.merge_range(row,col+4, row,col +3+4,"mardi" , cell_format) 
        worksheet.merge_range(row,col+4+4, row,col +3+8,"mercredi" , cell_format) 
        worksheet.merge_range(row,col+4+8, row,col +3+12,"jeudi" , cell_format) 
        worksheet.merge_range(row,col+4+12, row,col +3+16,"vendredi" , cell_format) 

        # Start from the first cell. Rows and columns are zero indexed.
        row = 1
        col = 1
        cj = 0# compteur de matin ou d'apres midi
        # Iterate over the data and write it out row by row
        for i in range(0,10):# i la demi journé
            #print(i)
            
            hour = 0
            try:
                #print(planning[0][i][0])
                for j in planning[0][i][0]: # calcul du nombre d'heure dans une demi-journée
                    #print(j["duration"])
                    hour += j["duration"]
            except:
                pass
                #print("1")   

            if cj == 2:# si nouvelle journée
                col +=4
                row = 1 
                cj = 0 #comteur

            if i%2 == 0:# si matin
                if hour < 4:
                    row =5- hour

            if i%2 == 1:# si apres-midi
                if row <4:
                    row = 5
                # 
                cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1,'fg_color': 'white'}) 
                worksheet.merge_range(row,col, row + 1 ,col +3,"déjeuner" , cell_format)        
                row += 2   
            try:  
                for j in planning[0][i][0]: #j le cours selectionné
                    cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1})
                
                
                    ######### Gerer les couleurs ######
                    try:
                        if j["name"] == "maths":
                            cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1,'fg_color': 'red','text_wrap': True}) 
                    
                        elif j["name"]  == "informatique":
                            cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1,'fg_color': 'yellow','text_wrap': True})

                        elif j["name"]  == "comunication":
                            cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1,'fg_color': 'cyan','text_wrap': True})
                    
                        elif j["name"]  == "physique":
                            cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1,'fg_color': 'orange','text_wrap': True})
                    
                        elif j["name"] == "mandarin":
                            cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1,'fg_color': 'green','text_wrap': True})
                    
                        elif j["name"]  == "SI":
                            cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1,'fg_color': 'blue','text_wrap': True})
                    
                        elif j["name"] == "anglais":
                            cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1,'fg_color': 'pink','text_wrap': True})
                    
                        elif j["name"] == "DS":
                            cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1,'fg_color': 'purple','text_wrap': True})
                    
                        ##### Si la matiere n'existe pas on prend une couleur hashé conforme #######  
                        else:
                            cell_format = workbook.add_format({'align': 'center','valign': 'vcenter','border': 1,'fg_color': "#" + str(abs(hash(j["name"])))[0:6],'text_wrap': True})
                    

                        bold = workbook.add_format({'bold': True})
                    
                        ######## Texte à ecrire dans chaque case ########
                        texttowrite =str(j["name"]) + " " + str(j["type"]) + "\r\n" + str(j["prof"]) + "\r\n" + str(j["salle"])
                    
                   
                        ###### Ecris la case à l'emplacement corespondant ######   
                        try:

                            if j["divisions"] == 4:
                                texttowrite =str(j["name"]) + " " + str(j["type"]) + "\r\n" + str(j["prof"][0]) + "\r\n" + str(j["salle"][0])
                                if j["duration"] !=1:
                                    worksheet.merge_range(row,col+0, row + int(j["duration"])-1 ,col +0,texttowrite +str(j["groupe"][0]), cell_format)
                                    worksheet.merge_range(row,col+1, row + int(j["duration"])-1 ,col +1,texttowrite +str(j["groupe"][1]), cell_format)                        
                                    worksheet.merge_range(row,col+2, row + int(j["duration"])-1 ,col +2,texttowrite +str(j["groupe"][2]), cell_format)                        
                                    worksheet.merge_range(row,col+3, row + int(j["duration"])-1 ,col +3,texttowrite +str(j["groupe"][3]), cell_format)
                                else:
                                    worksheet.write(row,col +0,texttowrite +str(j["groupe"][0]),cell_format)
                                    worksheet.write(row,col +1,texttowrite +str(j["groupe"][1]),cell_format)
                                    worksheet.write(row,col +2,texttowrite +str(j["groupe"][2]),cell_format)
                                    worksheet.write(row,col +3,texttowrite +str(j["groupe"][3]),cell_format)
                                                     
                       
                            elif j["divisions"] == 3:
                                texttowrite =str(j["name"]) + " " + str(j["type"]) + "\r\n" + str(j["prof"][0]) + "\r\n" + str(j["salle"][0])
                         
                                if j["duration"] !=1:
                                    worksheet.merge_range(row,col+0, row + int(j["duration"])-1 ,col ,texttowrite , cell_format)
                                    worksheet.merge_range(row,col+1, row + int(j["duration"])-1 ,col +1,texttowrite, cell_format)  
                                    worksheet.merge_range(row,col+2, row + int(j["duration"])-1 ,col +3,texttowrite +str(j["groupe"][1]), cell_format)  
                                else:
                                    worksheet.write(row,col +0,texttowrite,cell_format)
                                    worksheet.write(row,col +1,texttowrite,cell_format)                      
                                    worksheet.merge_range(row,col+2, row  ,col +3,texttowrite , cell_format) 


                            elif j["divisions"] == 2:
                                texttowrite =str(j["name"]) + " " + str(j["type"]) + "\r\n" + str(j["prof"][0]) + "\r\n" + str(j["salle"][0])
                        
                                worksheet.merge_range(row,col+0, row + int(j["duration"])-1 ,col+1 ,texttowrite +str(j["groupe"][0]), cell_format)
                                worksheet.merge_range(row,col+2, row + int(j["duration"])-1 ,col +3,texttowrite +str(j["groupe"][1]), cell_format)  
                       
                            else:

                                worksheet.merge_range(row,col, row + int(j["duration"])-1 ,col +3,texttowrite , cell_format)
                    
                            row += j["duration"]-1 # La nouvelle ligne se place en ajoutant le nombre d'heure
                   
                            ##########################

                            row += 1 # on passe à la ligne suivante
                        except:
                            print("error ici")
                    except:
                        pass
                        #print("list vide") #exception si la list est vide 
                #input()
                    #print("test fin de list", j," la demi journé : ",i,planning[0])   
                cj+=1 # incrémentation de demi journee
            except:
                pass
                #print("2")

        #print(self.__plannings)
        #print("dernier test",planning)

        workbook.close() #fermeture du excel.
        #input()
            

###################################

def main():
    print('Le travail est fini')

if __name__ == "__main__": main()
