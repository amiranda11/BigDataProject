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
#Identificando el tipo encontrando la palabra clave
def evaluate_text(s):
    type = []
    index = 0
    sentce = s.split(" ")
    blocked = [ '' ,'me' , 'you' , 'us' , 'we' , 'I' , 'are' , 'if', 'the' , 'or' , 'in', 'are' , 'is' , '!' , '?' , '@']
    for word in sentce:
        #Ignoring me, the, of, /n or ''
        for i in blocked:
            if(word == i):
            continue
        #Analyzing the key words
        if(word == 'power'):
            type = analyzePower(s,sentce, index)
        elif (word == 'internet'):
            type = analyzeCommunication(s,sentce, index)
        elif (word == 'signal'):
            type = analyzeCommunication(s,sentce, index)
        elif (word == 'tv'):
            type = analyzeCommunication(s,sentce, index)
        elif (word == 'water'):
            type = analyzeWater(s, sentce, index)
        elif (word == 'wastewater'):
            type = analyzeWasteWater(s, sentce, index)
        elif (word == 'drainage' ):
            type = analyzeWasteWater(s, sentce, index)
        elif (word == 'evac'):
            type = analyzeWasteWater(s, sentce, index)
        elif (word == 'evacuation'):
            type = analyzeWasteWater(s, sentce, index)
        elif(word == 'transportation'):
            type = analyzeTransportation(s, sentce, index)
        elif(word == 'vehicular'):
            type = analyzeTransportation(s, sentce, index)
        elif(word == 'trafic'):
            type = analyzeTransportation(s, sentce, index)
        elif(word == 'bridge'):
            type = analyzeTransportation(s, sentce, index)
        elif(word == 'road'):
            type = analyzeTransportation(s, sentce, index)
        else:
            pass
    #type = analyzeOther(s, sentce)
    index+=1
    return type
        


# Power - 1
def analyzePower(txt, s, index):
    if(s[index-1] or s[index+1] == "not" or "off" or "down" or "fallen" or "cables" or "service" or "lost"):
        return [txt, 1,1]
    elif(s[index-1] or s[index+1] == "back"):
        return [txt, 1,0]
    elif(s[index-1] or s[index+1] == "back"):
        return [txt, 1,0]
    elif(s[index-1] == "have" or s[index+1] == "back"):
        return [txt, 1,0]
    else:
        return [txt, 7,0]

# Communication - 2   
def analyzeCommunication(txt, s, index):
    if(s[index-1] or s[index+1] == "no" or "issue"):
        return [txt, 2, 1]
    else:
        return [txt, 2, 0]

# Water - 3
def analyzeWater(txt, s, index):
    if(s[index -2] or s[index-1] == "bottle" or " bottled"):
        if(s[index -3] == "last"):
            return [txt, 3,1]
    else:
        return [txt, 3, 0]
# Wastewater - 4   
# Mejorar 
def analyzeWasteWater(txt,s, index):
    if(s[index -2] or s[index-1] == "bottle" or " bottled"):
        if(s[index -3] == "last"):
            return [txt, 3,1]
    else:
        return [txt, 3, 0]

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
        if(word == "Hurricane" or "Irma"):
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
    outputResult.append(evaluate_text(i))


for i in outputResult:
    print (i)

#output code

'''
with open('outputResults.csv', mode='w') as csv_file:
    fieldnames = ['ï»¿text', 'disruption_type', 'disruption_status']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    count = 0
    writer.writeheader()
    for results in outputResult:
        writer.writerow({'ï»¿text': outputResult[count][0], 
        'disruption_type': outputResult[count][1], 'disruption_status': outputResult[count][2]})
'''
