# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 23:14:28 2025

@author: lupin
"""

import os
import sys

if getattr(sys, 'frozen', False):#si le programme est frozen (exe)
    base_path = os.path.dirname(sys.executable)  # dossier de l'exe
else:#le programme marche en python classique
    base_path = os.path.dirname(os.path.abspath(__file__))
    
questionVersReponse = {}
questionVersScore = {}
questionVersAEteLu = {}

fichier_path = os.path.join(base_path, "questionsReponses.txt")

with open(fichier_path, encoding="latin-1") as fichier:
    for line in fichier :
        line = line.split('/')
        question = line[0].encode('latin-1')
        reponse = line[1].encode('latin-1')
        score = int(line[2])
        questionVersReponse[question] = reponse
        questionVersScore[question] = score
        questionVersAEteLu[question] = False

sortedDic = sorted(questionVersScore.items(), key=lambda item: item[1], reverse=True)
#un premier tri au cas où des éléments aient été ajoutés dans le fichier entre temps

for item in sortedDic :
        question = item[0]
        print(item[0].decode('utf8'))
        getAnswer = input()
        isAnswered = input("La réponse était "+questionVersReponse[question].decode('utf8')+", bien répondu ? Indiquer o pour oui \n")
        if isAnswered == "o" :
            nouveauScore = 0
        elif isAnswered == "exit" :
            break
        else :
            nouveauScore = int(questionVersScore[question]) + 1
        questionVersScore[question] = nouveauScore
        questionVersAEteLu[question] = True
        #for i in range(5) :
        #    print(LINE_UP, end = LINE_CLEAR)
        clear = lambda: os.system('cls')
        clear()

#On rajoute 1 à toutes les questions qui n'ont pas été vues
for question in questionVersScore.keys() :
    if questionVersAEteLu[question] == False :
        questionVersScore[question] += 1

sortedDic = sorted(questionVersScore.items(), key=lambda item: item[1], reverse=True)
#un second tri avant de réécrire

with open(fichier_path, "w", encoding="latin-1") as fichier:
    for item in sortedDic :
        question = item[0]
        line = question.decode('latin-1')+"/"+questionVersReponse[question].decode('latin-1')+"/"+str(questionVersScore[question])+"/"+"\n"
        fichier.write(line)