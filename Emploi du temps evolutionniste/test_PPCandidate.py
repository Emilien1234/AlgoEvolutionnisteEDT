import unittest
import xlsxwriter
import json
from PPCandidate import *
from random import *
import os
import time
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear') # pour pouvoir effacer la console :)



class TestConstructor(unittest.TestCase):

    def test_creation(self):
        can = Candidate()
        self.assertEqual(len(can.get_content()), 4, "wrong amount of semesters")
        self.assertEqual(len(can.get_content()[0]), 10, "wrong amount of slots per semester")

    def test_add_course_valid(self):
        can = Candidate()
        course = {"name": "mathematics", "type": "cm", "duration": 2, "prof": ["RC"], "division": 1, "constraints": [0, 1]}
        can.add_course(course, 0, 0)
        self.assertEqual(can.get_content()[0][0][0][0]["name"], "mathematics")




def newEmploiDuTemps():

    cost = 0
    heure =""

    with open("heure.json","r") as f:  #ouvre le nombre d'heure à caser et stock dans heures on pourais utiliser  nottre tools mais pour deux lignes...
        heure = json.load(f) # provient de notre fichier d'entrée


    courstemp = [] #list de tuple ou stoquer notre emploi du temps et notre varialbe de cout

    hr = 0 # nombre d'heure a caser dans la semaine

    for i in heure["cours"]: # 
        a = i,int(heure["cours"][i]["heure"]) # var temp pour stoquer emp et cost
        courstemp.append(a) #courstemp contient toute les coruse avec les heure a mettre dans une semaine
        hr += a[1] #nombre d'heure restante
    
    #print("test",courstemp,"heure : " , hr)
    
    can = Candidate() # notre classe

    while hr !=0: #tant qu'il reste des heure a mettre

        djc = randint(0,9) #demi journées choisie au hasard
        cc = randint(0,len(courstemp)-1) #cours choisie au hasard
        i = courstemp[cc][1] # nombre d'heure dans la matiere
        d = 0 # duree du cours

        if i >= 4: # si il y a plus de 4 heure d'un cours a caser on randomise entre 1 et 4 
            d = randint(1,4)
        else:
            d = randint(1,courstemp[cc][1])

        courstemp[cc] = courstemp[cc][0],courstemp[cc][1]-d
        
        
        hr -= d #en enleve dle nombre d'heure restante
        
        # on crée un nouveau cours avec les valeurs trouvées
        coursImp =  heure["cours"][courstemp[cc][0]]
        course = {"name": courstemp[cc][0] , "type": "cm", "duration": d, "prof":coursImp["prof"],"contrainte":coursImp["contrainte"],"salle":coursImp["salle"],"divisions":coursImp["divisions"] if "divisions" in coursImp else 1,"groupe":coursImp["groupe"] if "groupe" in coursImp else 0} # tres tres sale.
        
        #  et on l'ajoute à notre classe

        can.add_course(course, 0, djc) #cours, semestre, index


        if courstemp[cc][1] == 0: # si le nombre d'heure d'une matinee est de zero on la retire de la list
            courstemp.pop(cc)

    emp = can.get_course() # on stoque l'emploi du temps ainsi crée dans une variable

    cost = can.cost(emp) # on demande le poids de l'empoi du temps ainsi crée
    
    can.efface() #On l'efface ?

     
    return cost,emp # On renvoi la valeur de l'emploi du temps ainsi que l'emploi du temps


def ptage(nedt,pr_g,ng): # fonction de calcule du nombre totale d'emploidu temps crée pour l'affichage
    return (nedt-(int(nedt/pr_g)-1))*(ng-1)+nedt

if __name__ == '__main__': # main ???
    try:
        unittest.main()
    except : 
        print ("error") # Mon logiciel revoi une erreur peut importe le contenue... une fois lancé. 

    c = 0 # compteur du nombre de generation.
    ng = 10#nombre  de génération
    nedt = 100 # nombre d'emploi du temps a crée par generation
    pr_g = 20 # precision à supruimer a chaque genereation

    ng = int(input("Amount of génération (> 10) : "))
    pr_g = int(input("Precision (2 < valeur < 30) : ")) # en vrai c'est pas la précision mais c'est ce qui s'en aproche le plus :)

    nbmax = ptage(nedt,pr_g,ng) #nombre de generation max
    print("Amount of element to generate :",nbmax)

    edt = [] # liste d'emploi du temps

    ct = 0 # compteur
    lb = "" # ?
    can = Candidate()

    start_time = time.time() # temps du debut du programme


    for nbessai in range(0,ng): # boucle de generation
        for i in range(0,nedt-len(edt)):

            edt.append(newEmploiDuTemps())
            can.efface()
            c+=1
            #clear() # effet de chargement ultra stylé mais incroyablement lent :(
            if round((c*100/nbmax),2)>ct:

                ################# Affichage ##############"

                clear()
                print("Travail effectué à :",ct,"%,","pour l'emploi du temps numéro : ",str(c)+"/" +str(nbmax))
                
                lb ="■"*(int(ct/10))+" "*(10-(int(ct/10)))
                print("[",lb,"]")
                #"""■"
                ct+=10
                ##########################################



        #classement des meilleurs emploi du temps avec lamba bien plus efficace ici qu'un def et plus claire qu'une liste avec des truc dedans 
        edt.sort(key=lambda tup: tup[0])
        
        # on ne garde que la totalité divisé par la précision des derniers

        del(edt[int(len(edt)/pr_g)-1:])
        #print(edt[1])

    # On genere les deux meilleur emploi du temps.
    can.write_xlsx("semsester 1-2.xlsx",edt[1][1])
    can.write_xlsx("semsester 1_1.xlsx",edt[0][1])
    #clear()
    print("Score of the best planning :",edt[0][0])
    print("Execution time : %s seconde" % round((time.time() - start_time),2))


    can.save_schedules("save_best_emp",edt[0][1]) #enregistre l'emploi du temps
    
    with open("save_best_emp.json","r") as fjson:  #o
            
            a = (json.load(fjson))# lis l'emploi du temps
            

    can.write_xlsx("ouverture.xlsx",a)#stock emploi du temps enregistré
    input("pause...")
    #input ("Que faire ?")
