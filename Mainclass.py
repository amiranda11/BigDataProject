#BigData Project
#Contributos: Abiesel, Ramphis, Alexander, Laizla & Andrea

#imports
import csv


#input code
file_tweets = []
file_name = input("Enter the file name: ")

default_file_name = 'ASCE_Samples_v2.csv' 
if(len(file_name)<= 1):
    file_name = default_file_name

with open(file_name) as File:
    reader = csv.DictReader(File)
    for row in reader:
        file_tweets.append(row)
'''
    for loop saves every sentences
'''
sentences = [] #Contains every sentences of each row
counter = 0
for i in file_tweets:
    sentences.append(file_tweets[counter]['ï»¿text'])
    counter+= 1



#Text Analysis
"""
    Disruption Type: 
        hurricane related:
            power: 1, communication: 2, water: 3, wastewater: 4, transportation : 5,  other -:6
    
        hurricante not related: 7

    Disruption Status:
        actual disruption - 1
        not disruption - 0
"""

'''
tweetlistHR = {'hurricane': [], 'water': [], 'power': [], 'communication': [], 'wastewater': [], 'transportion':[], 'other': []}

tweetlistHR['hurricane'] = ["hurricane Irma", "hurricane"]
tweetlistHR['water'] = ["bottle of water", "drinking water", "water", "bottled water"]
tweetlistHR['power'] = ["power off", "power down", "lost power", "fallen power service", 
                "fallen power cables", "fallen power spot", "power back", "power is back",
                ]
'''
def evaluate_text(s, l):
    rslt = []
    founded = False
    for word in s.split():
        for i in l:
            if(word == i):
                founded = True
                return 
    
    return True


def assign_type(s):
    if s == 'power':
        return 1
    elif s == 'communication':
        return 2
    elif s == 'water':
        return 3
    elif s == 'wastewater':
        return 4
    elif s == 'transportation':
        return 5
    elif s == 'other':
        return 6
    else:
        return 7


'''
Array que tiene en el indice [0] el type y en el indice [1] el status
La funcion del output tiene que evaluar la lista y por cada i escribir
en el csv file el texto, el type y el status

'''
#ouputResult = [s, assign_type(s), assign_status(s)]


#output code


