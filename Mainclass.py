#BigData Project
#Contributos: Abiesel, Ramphis, Alexander, Laizla & Andrea

#imports
import csv

#from sklearn.feature_extraction.text import CountVectorizer

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
        
#for loop saves every sentences in sentence[]

sentences = [] #Contains every sentences of each row
counter = 0
for i in file_tweets:
    sentences.append(file_tweets[counter]['ï»¿text'])
    counter+= 1

#MainClass 
    

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

def clean_txt(s):
    s = s.lower()
    sentce =s.split(" ")
    blocked = [ '' ,"me", "Me" , "you" , "us" , "we" , "I","u", "they", "are", "they're", "if", "the", "an", "a"
    'or' , 'in', 'are' , 'is' , '!' , '?' , '@', "It's", "my", "to", "of",  "like"]
    index = 0
    for word in sentce:
        #Ignoring me, the, of, /n or ''
        for i in blocked:
            if(word == i):
                sentce.pop(index)
        index+=1
    return sentce





#Identificando el tipo encontrando la palabra clave
def evaluate_text(s,sentce, tag):
    #Analyzing the key words
    if(tag[0] == "power"):
        type = analyzePower(s,sentce, tag[1])
    elif (tag[0] == "communication"):
        type = analyzeCommunication(s,sentce, tag[1])
    elif (tag[0] == "water"):
        type = analyzeWater(s, sentce, tag[1])
    elif (tag[0] == "wastewater"):
        type = analyzeWasteWater(s, sentce, tag[1])
    elif(tag[0] == 'transportation'):
        type = analyzeTransportation(s, sentce, tag[1])
    else:
        type = analyzeOther(s, sentce)

    return type

#Tagging
def tagging(txt):
    result = []
    index = 0
    for word in txt:
        if(word == 'power'):
            return ["power", index]
        elif(word == 'generator'):
            return ["power", index]
        elif (word == 'internet'):
            return ["communication", index]
        elif (word == 'signal'):
            return  ["communication", index]
        elif (word == 'tv'):
             return["communication", index]
        elif (word == 'water'):
            return   ["water", index]
        elif (word == 'wastewater'):
            return   ["wastewater", index]
        elif (word == 'drainage' ):
            return   ["wastewater", index]
        elif (word == 'evac'):
            return   ["wastewater", index]
        elif (word == 'evacuation'):
            return   ["wastewater", index]
        elif(word == 'transportation'):
            return   ["transportation", index]
        elif(word == 'vehicular'):
            return  ["transportation", index]
        elif(word == 'trafic'):
            return  ["transportation", index]
        elif(word == 'bridge'):
            return ["transportation", index]
        elif(word == 'road'):
            return ["transportation", index]
        else:
            result = ["other", index]
        index+=1
    return result

#Analisis
# Power - 1
def analyzePower(txt, s, index):
    #negative
    if(s[index-1]  == "not"):
        return [txt, 1,1]
    elif(s[index-1]  == "off"):
        return [txt, 1,1]
    elif(s[index-1]  == "down"):
        return [txt, 1,1]
    elif(s[index-1]  == "fallen"):
        return [txt, 1,1]
    elif(s[index-1]  == "without"):
        return [txt, 1,1]
    elif(s[index-1]  == "out"):
        return [txt, 1,1]
    elif(s[index-1]  == "lost"):
        return [txt, 1,1]
    #falta los que tienen word= power pero no son hurricane related
    else:
        return [txt,1 ,0]

# Communication - 2   
def analyzeCommunication(txt, s, index):
    if(s[index-1] == "no"):
        return [txt, 2, 1]
    elif(s[index-1] == "issue"):
        return [txt, 2, 1]
    else:
        return [txt, 2, 0]


# Water - 3
def analyzeWater(txt, s, index):
    if(s[index-1] == "bottle"):
        if(s[index -3] == "last"):
            return [txt, 3,1]
    elif(s[index-1] == "bottled"):
        if(s[index -3] == "last"):
            return [txt, 3,1]
        return [txt, 3, 0]
    else:
        return [txt, 3, 0]

# Wastewater - 4   
# Mejorar 
def analyzeWasteWater(txt,s, index):
    if(s[index -1] == "bottle" ):
        if(s[index -3] == "last"):
            return [txt, 4,1]
    else:
        return [txt, 4, 0]

#Transportation - 5    
def analyzeTransportation(txt,s, index):
    if(s[index] == "bridge"):
        if(s[index-1] or s[index+1] == "closed" or "collapsed" or "fallen"):
            return [txt, 5,1]
        else:
            return[txt, 5,0]
    elif(s[index] == "traffic"):
        if(s[index-1] or s[index+1] == "unnecessary" or "congestion" or "fallen"):
            return [txt, 5,1]
        else:
            return[txt, 5,0]
    elif(s[index] == "highway"):
        return [txt, 5, 0]
    else:
        return [txt, 5, 0]
    
#Other but hurricanre relate- 6; Not hurricane relate - 7
def analyzeOther(txt, s):
    for word in s:
        if(word == "Hurricane"):
            return [txt, 6, 0]
        elif(word == "storm"):
            return [txt, 6, 0]
        else:
            return [txt, 7, 0]

'''
Array que tiene en el indice [0] el type y en el indice [1] el status
La funcion del output tiene que evaluar la lista y por cada i escribir
en el csv file el texto, el type y el status

'''
#outputResult = [[s, assign_type(s), assign_status(s)]]
outputResult = []
#Main
index = 0
for i in sentences:
    cleanedtxt = clean_txt(i)
    tag = tagging(cleanedtxt)
    outputResult.append(evaluate_text(i, cleanedtxt, tag))


for i in outputResult:
    print (i)



#output code
with open('outputResults.csv', mode='w') as csv_file:
    fieldnames = ['ï»¿text', 'disruption_type', 'disruption_status']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    count = 0
    writer.writeheader()
    for results in outputResult:
        writer.writerow({'ï»¿text': outputResult[count][0], 'disruption_type': outputResult[count][1], 'disruption_status': outputResult[count][2]})
        count+=1
      
