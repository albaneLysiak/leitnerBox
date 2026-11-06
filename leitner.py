# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 23:14:28 2025

@author: lupin
"""

import os
import sys

def clear_terminal() :
    os.system("cls" if os.name == "nt" else "clear")

if getattr(sys, 'frozen', False):#if the program is frozen (exe)
    base_path = os.path.dirname(sys.executable)  # exe file
else:#the program works in classic python mode
    base_path = os.path.dirname(os.path.abspath(__file__))
    
questionToAnswer = {}
questionToScore = {}
questionToWasRead = {}

fichier_path = os.path.join(base_path, "questionsReponses.txt")

with open(fichier_path, encoding="latin-1") as fichier:
    for line in fichier :
        line = line.split('/')
        question = line[0].encode('latin-1')
        reponse = line[1].encode('latin-1')
        score = int(line[2])
        questionToAnswer[question] = reponse
        questionToScore[question] = score
        questionToWasRead[question] = False

sortedDic = sorted(questionToScore.items(), key=lambda item: item[1], reverse=True)
#a first sorting in case elements were added to the questions and answers file between two executions

for item in sortedDic :
        question = item[0]
        print(item[0].decode('utf8'))
        getAnswer = input()
        isAnswered = input("La réponse était "+questionToAnswer[question].decode('utf8')+", bien répondu ? Indiquer o pour oui \n")
        if isAnswered == "o" :
            nouveauScore = 0
        elif isAnswered == "exit" :
            break
        else :
            nouveauScore = int(questionToScore[question]) + 1
        questionToScore[question] = nouveauScore
        questionToWasRead[question] = True
        clear_terminal()

#A score of 1 is added to all the questions that were not seen
for question in questionToScore.keys() :
    if questionToWasRead[question] == False :
        questionToScore[question] += 1

sortedDic = sorted(questionToScore.items(), key=lambda item: item[1], reverse=True)
#a second sorting before the rewriting

with open(fichier_path, "w", encoding="latin-1") as fichier:
    for item in sortedDic :
        question = item[0]
        line = question.decode('latin-1')+"/"+questionToAnswer[question].decode('latin-1')+"/"+str(questionToScore[question])+"/"+"\n"
        fichier.write(line)