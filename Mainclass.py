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

    
"""
index = 0
for i in sentences:
    rst = i.split(" ")
    print(rst)
    index +=1

"""
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
    sentce = s.split(" ", ".")
    for word in sentce:
        if(word == 'power'):
            type = analyzePower(sentce, index)
        elif (word == 'internet' or 'signal' or 'tv'):
            type = analyzeCommunication(sentce, index)
        elif (word == 'water'):
            type = analyzeWater(sentce, index)
        elif (word == 'wastewater' or 'drainage' or 'evac' or 'evacuation'):
            type = analyzeWasteWater(sentce, index)
        elif(word == 'hurricane'):
            type = analyzeOther(sentce, index)
        elif( word == 'Irma'):
            type = analyzeOther(sentce, index)
        elif(word == 'transportation' or 'trafic'or 'vehicular'):
            type = analyzeTransportation(sentce, index)
        elif(word == 'bridge'):
            type = analyzeTransportation(sentce, index)
        elif(word == 'road'):
            type = analyzeTransportation(sentce, index)
        
        else:
            type = analyzeOther(sentce, index)
        index += 1
    return type


# Power - 1
def analyzePower(s, index):
    if(s[index-1] or s[index+1] == "not" or "off" or "down" or "fallen" or "cables" or "service" or "lost"):
        return [1,1]
    elif(s[index-1] or s[index+1] == "back"):
        return [1,0]
    elif(s[index-1] or s[index+1] == "back"):
        return [1,0]
    elif(s[index-1] == "have" or s[index+1] == "back"):
        return [1,0]
    else:
        return [7,0]

# Communication - 2   
def analyzeCommunication(s, index):
    if(s[index-1] or s[index+1] == "no" or "issue"):
        return [2, 1]
    else:
        return [2, 0]

# Water - 3
def analyzeWater(s, index):
    if(s[index -2] or s[index-1] == "bottle" or " bottled"):
        if(s[index -3] == "last"):
            return [3,1]
    else:
        return [3, 0]
# Wastewater - 4   
# Mejorar 
def analyzeWasteWater(s, index):
    if(s[index -2] or s[index-1] == "bottle" or " bottled"):
        if(s[index -3] == "last"):
            return [3,1]
    else:
        return [3, 0]

#Transportation - 5    
def analyzeTransportation(s, index):
    if(s[index] == "bridge"):
        if(s[index-1] or s[index+1] == "closed" or "collapsed" or "fallen"):
            return [5,1]
        else:
            return[5,0]
    elif(s[index] == "traffic"):
        if(s[index-1] or s[index+1] == "unnecessary" or "congestion" or "fallen"):
            return [5,1]
        else:
            return[5,0]
    elif(s[index] == "highway"):
        return [5, 0]
    else:
        return [5, 0]
    
#Other but hurricanre relate- 6; Not hurricane relate - 7
def analyzeOther(s, index):
    if(s[index-1] or s[index+1] == "not" or "off or down" or "back"):
        return [6,1]
    elif(s[index-1] or s[index+1] == "fallen" or "cables" or "service"):
        return [6,0]
    else:
        return [7, 0]

'''
Array que tiene en el indice [0] el type y en el indice [1] el status
La funcion del output tiene que evaluar la lista y por cada i escribir
en el csv file el texto, el type y el status

'''
#ouputResult = [[s, assign_type(s), assign_status(s)]]

ouputResult = []

#output code

with open('outputResults.csv', mode='w') as csv_file:
    fieldnames = ['ï»¿text', 'disruption_type', 'disruption_status']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    count = 0
    writer.writeheader()
    for results in ouputResult:
        writer.writerow({'ï»¿text': ouputResult[count][0], 
        'disruption_type': ouputResult[count][1], 'disruption_status': ouputResult[count][2]})
