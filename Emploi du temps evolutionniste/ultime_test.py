import unittest

#from PPCandidate import *
from PPCandidate import *
from tools import *
#from tools_COR import *

import os.path
from os import path

from random import randint

class EvalLivrable1(unittest.TestCase):


    def init(self):
        coursP1 = []
        coursP1.append(dict({"name": "mathematics", "type": "cm", "duration": 2, "prof": ["RC"], "division": 1, "constraints": [0, 1]}))
        coursP1.append(dict({"name": "mathematics", "type": "cm", "duration": 2, "prof": ["RC"], "division": 1, "constraints": [6, 8, 9]}))
        coursP1.append(dict({"name": "mathematics", "type": "cm", "duration": 1, "prof": ["RC"], "division": 1, "constraints": [0, 1]}))
        coursP1.append(dict({"name": "mathematics", "type": "cm", "duration": 1, "prof": ["RC"], "division": 1, "constraints": [6, 8, 9]}))
        coursP1.append(dict({"name": "mathematics", "type": "td", "duration": 2, "prof": ["RC"], "division": 2, "constraints": [2, 3]}))
        coursP1.append(dict({"name": "mathematics", "type": "td", "duration": 2, "prof": ["RC"], "division": 2, "constraints": [4, 5]}))
        coursP1.append(dict({"name": "SI", "type": "cm", "duration": 2, "prof": ["GJ"], "division": 1, "constraints": [1, 2]}))
        coursP1.append(dict({"name": "SI", "type": "td", "duration": 2, "prof": ["GJ"], "division": 2, "constraints": [3, 4]}))
        coursP1.append(dict({"name": "SI", "type": "td", "duration": 2, "prof": ["GJ"], "division": 2, "constraints": [6]}))
        coursP1.append(dict({"name": "SI", "type": "tp", "duration": 2, "prof": ["GJ"], "division": 2, "constraints": [8, 9]}))
        coursP1.append(dict({"name": "physique", "type": "cm", "duration": 1, "prof": ["KR"], "division": 1, "constraints": [0, 1]}))
        coursP1.append(dict({"name": "physique", "type": "cm", "duration": 1, "prof": ["KR"], "division": 1, "constraints": [2, 3]}))
        coursP1.append(dict({"name": "physique", "type": "tp", "duration": 2, "prof": ["TF", "AT"], "division": 2, "constraints": [4, 5, 6]}))
        coursP1.append(dict({"name": "mecanique", "type": "cm", "duration": 2, "prof": ["MB"], "division": 1, "constraints": [6]}))
        coursP1.append(dict({"name": "anglais", "type": "cm", "duration": 2, "prof": ["IO"], "division": 2, "constraints": [4, 5]}))
        coursP1.append(dict({"name": "lv2", "type": "cm", "duration": 2, "prof": ["Unknown"], "division": 2, "constraints": [4, 5]}))
        coursP1.append(dict({"name": " ", "type": "free", "duration": 4, "prof": [" "], "division": 1, "constraints": [7]}))
        coursP1.append(dict({"name": "informatique", "type": "cm", "duration": 1, "prof": ["PA"], "division": 1, "constraints": [0, 1, 2, 3]}))
        coursP1.append(dict({"name": "informatique", "type": "info", "duration": 2, "prof": ["AP", "PA"], "division": 2, "constraints": [6, 8, 9]}))
        coursP1.append(dict({"name": "communication", "type": "td", "duration": 2, "prof": ["AL"], "division": 2, "constraints": [1, 2]}))
        coursP1.append(dict({"name": "DS", "type": "ds", "duration": 2, "prof": ["surveillant"], "division": 1, "constraints": [3]}))

        coursP2 = []
        coursP2.append(dict({"name": "mathematics", "type": "cm", "duration": 2, "prof": ["NM"], "division": 1, "constraints": [0, 1]}))
        coursP2.append(dict({"name": "mathematics", "type": "cm", "duration": 2, "prof": ["NM"], "division": 1, "constraints": [2, 3]}))
        coursP2.append(dict({"name": "mathematics", "type": "cm", "duration": 1, "prof": ["NM"], "division": 1, "constraints": [0, 1]}))
        coursP2.append(dict({"name": "mathematics", "type": "cm", "duration": 1, "prof": ["NM"], "division": 1, "constraints": [6, 8, 9]}))
        coursP2.append(dict({"name": "mathematics", "type": "td", "duration": 2, "prof": ["NM"], "division": 2, "constraints": [2, 3]}))
        coursP2.append(dict({"name": "mathematics", "type": "td", "duration": 2, "prof": ["NM"], "division": 2, "constraints": [4, 5]}))
        coursP2.append(dict({"name": "SI", "type": "cm", "duration": 2, "prof": ["GJ"], "division": 1, "constraints": [8, 9]}))
        coursP2.append(dict({"name": "SI", "type": "td", "duration": 2, "prof": ["GJ"], "division": 2, "constraints": [2, 3, 4, 5, 6]}))
        coursP2.append(dict({"name": "SI", "type": "td", "duration": 2, "prof": ["GJ"], "division": 2, "constraints": [5, 6, 8, 9]}))
        coursP2.append(dict({"name": "SI", "type": "tp", "duration": 2, "prof": ["TF"], "division": 3, "constraints": [1, 2]}))
        coursP2.append(dict({"name": "physique", "type": "cm", "duration": 1, "prof": ["KR"], "division": 1, "constraints": [2, 3]}))
        coursP2.append(dict({"name": "physique", "type": "cm", "duration": 1, "prof": ["KR"], "division": 1, "constraints": [4, 5]}))
        coursP2.append(dict({"name": "physique", "type": "tp", "duration": 2, "prof": ["TF", "AT"], "division": 3, "constraints": [4, 5, 6]}))
        coursP2.append(dict({"name": "anglais", "type": "cm", "duration": 2, "prof": ["IO"], "division": 3, "constraints": [1, 2]}))
        coursP2.append(dict({"name": "lv2", "type": "cm", "duration": 2, "prof": ["Unknown"], "division": 3, "constraints": [1, 2]}))
        coursP2.append(dict({"name": " ", "type": "free", "duration": 4, "prof": [" "], "division": 1, "constraints": [7]}))
        coursP2.append(dict({"name": "informatique", "type": "cm", "duration": 1, "prof": ["PA"], "division": 2, "constraints": [8, 9]}))
        coursP2.append(dict({"name": "informatique", "type": "tp", "duration": 2, "prof": ["AP", "PA"], "division": 3, "constraints": [4, 5, 6]}))
        coursP2.append(dict({"name": "communication", "type": "tp", "duration": 2, "prof": ["AL"], "division": 3, "constraints": [5, 6]}))
        coursP2.append(dict({"name": "DS", "type": "ds", "duration": 2, "prof": ["surveillant"], "division": 1, "constraints": [5]}))

        cours = []
        cours.append(coursP1)
        cours.append(coursP2)

        return cours

    def test_functions_textfile(self):
        note = 0
        try:
            write_to_textfile("test.txt", "0000")
            note += 1
            if(path.exists("test.txt")):
                note += 1
        except:
            print("probleme dans write_to_textfile")
        try:
            _ = import_from_textfile("test.txt")
            note += 1
            note += 1
        except:
            print("problme dans import_from_textfile")
        try:
            write_to_textfile("test.txt", "0000")
            if(import_from_textfile("test.txt") == ["0000"]):
                note +=1
                note +=1
        except:
            print("probleme : fichier test introuvable")

        data = {"apple" : 6, "orange" : 4, "sushi" : 18}
        try:
            dump_to_binary("test.pickle", data)
            note += 1
            if(path.exists("test.pickle")):
                note += 1
        except:
            print("probleme dans dump_to_binary")
        try:
            load_from_binary("test.pickle")
            note += 1
            note += 1
        except:
            print("probleme dans load_from_binary")
        try:
            dump_to_binary("test.pickle", data)
            if(load_from_binary("test.pickle")["sushi"] == data["sushi"]):
                note += 1
                note += 1
        except:
            print("probleme : fichier test introuvable")

        try:
            savexlsx("testxlsx", "data", 1, 1, 5, 3)
            note += 1
            note += 1
            if(path.exists("testxlsx")):
                note += 1
            if(path.exists("testxlsx.xlsx")):
                note += 1
        except:
            print("probleme xlsx writer")

        print("test tools : {}/15 (jusqu'à 12 points peuvent être ajouté lors de l'évaluation)".format(note))


    def test_PPCandidate_full(self):
        note = 0
        try:
            can = Candidate()
            note += 1
        except:
            print("probleme dans le constructeur de PPCandidate")
        try:
            can = Candidate()
            if(len(can.get_content()) == 4):
                note += 1
            if(len(can.get_content()[0]) == 10):
                note += 1
        except:
            print("probleme dans la structure du planning ou get_content")

        data = self.init()
        can = Candidate()
        try:
            can = Candidate()
            can.add_course(data[0][0], 0, 0)
            note += 1
        except:
            print("probleme dans add_course")
        try:
            can = Candidate()
            can.add_course(data[0][0], 0, 0)
            _ = can.get_content()[0][0][0][0]["name"]
            note += 1
        except:
            print("probleme dans la structure du planning")
        try:
            can = Candidate()
            can.add_course(data[0][0], 0, 0)
            if(can.get_content()[0][0][0][0]["name"] == "mathematics"):
                note += 1
        except:
            print("probleme dans la structure du planning")

        can = Candidate()
        try:
            course = ["name", "mathematics"]
            if(can.add_course(course, 0, 0)== 3):
                note += 1
        except:
            print("probleme dans le code erreur")
        try:
            if(can.add_course(data[0][0], 4, 0)== 2):
                note += 1
        except:
            print("probleme dans le code erreur")
        try:
            if(can.add_course(data[0][0], 0, 10)== 1):
                note += 1
        except:
            print("probleme dans le code erreur")

        can = Candidate()
        for i, prom in enumerate(data):
            for j, cours in enumerate(prom):
                can.add_course(cours, 2*i, randint(0,9))
                can.add_course(cours, 2*i+1, randint(0,9))

        try:
            can.disp_schedules()
            note += 1
        except:
            print("probleme d'affichage du planning")
        try:
            can.save_schedules("planning.pickle")
            if(path.exists("planning.pickle") or path.exists("planning")):
                note += 1
        except:
            print("probleme de sauvegarde")
        try:
            can.write_xlsx("edt")
            if(path.exists("edt.xlsx") or path.exists("edt")):
                note += 1
        except:
            print("probleme de xlsx")

        temp = can.cost()
        note += 1
        note += 1
        print(temp)
        if(temp>0):
            note += 1
        #except:
        #    print("probleme dans la fonction de cout")


        print("PPCandidate test : {}/15 (jusqu'à 12 points peuvent être ajouté lors de l'évaluation)".format(note))


if __name__ == '__main__':
    
    print(import_from_textfile("a"))
    try:

        unittest.main()
    except:
        pass

