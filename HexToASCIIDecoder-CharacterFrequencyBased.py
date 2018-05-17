#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 17:30:14 2017

@author: Razorin
"""






def hexToBytes(hexa):
    
    b = bytes.fromhex(hexa)
    
    return list(b)



#key est un 8-bits bytes entré sous la forme d'un nombre compris entre 0 et 255
def singleByteXorHexa(x, key):
    
    binKey = str('0'* (8 - (len(bin(key)[2:])))) + str(bin(key)[2:])
    x = hexToBytes(x)
    decoded = ''
    xBin = ''
    finalBinKey = ''
    
    #Conversion des bytes en 8-bits
    for i in range(len(x)):
       xBin = str(xBin) + str('0'* (8 - (len(bin(x[i]) [2:])))) + str( bin(x[i]) [2:] )
       finalBinKey = finalBinKey + binKey
           
    for i in range(len(xBin)):
        if xBin[i] == finalBinKey[i]:
            decoded = decoded + '0'
        else:
            decoded = decoded + '1'
            
    #Decoded est en bits bruts -> conversion en sequences de 8-bits bytes pour passage en ASCII
    decoded_bytes = (decoded[i:i+8] for i in range(0, len(decoded), 8))
    #Condage en ASCII
    decoded = ''.join(chr(int(char, 2)) for char in decoded_bytes)
    
    return decoded
    


#Create a dictionnary to store the result of each key test.
testResults = {'key' : 'score'}

standardFrequencies = {'e':12.702,
                       "t":9.05,
                       "a"	:8.16,
                       "o"	:7.50,
                       "i"	:6.96,
                       "n"	:6.74,
                       "s"	:6.32,
                       "h"	:6.09,
                       "r"	:5.98,
                       "d"	:4.25,
                       "l"	:4.02,
                       "c"	:2.78,
                       "u"	:2.75,
                       "m"	:2.40,
                       "w"	:2.36,
                       "f"	:2.22,
                       "g"	:2.01,
                       "y"	:1.97,
                       "p"	:1.92,
                       "b"	:1.49,
                       "v"	:0.97,
                       "k"	:0.77,
                       "j"	:0.15,
                       "x"	:0.15,
                       "q"	:0.09,
                       "z"	:0.07}



#Plus le score est proche de 0, meilleur c'est
def scoring(sentence):
    
    occurrences = {}
    score = 0
    sentence = str(sentence).lower()
    
    for i in sentence:
        #Ne prend en compte que les caractères alpahnumériques et pas l'espace
        if i.isalpha():
            if i in occurrences.keys():
                occurrences[i] = occurrences[i] + 1
            else:
                occurrences[i] = 1
            
    for i in occurrences.keys():
        occurrences[i] = ( occurrences[i]/len(sentence) ) * 100
    
    for i in standardFrequencies.keys():
        if i in occurrences.keys():
            score = score + abs(standardFrequencies[i] - occurrences[i])
        else :
            score = score + standardFrequencies[i]
    
    return score
            
       
    

def testKeys(x):
    
    testResults = {}
    result = [ '' for i in range(0,256)]
    
    for i in range(0,256):
        result[i] = singleByteXorHexa(x, i), i
        score = scoring(result[i])
        testResults[result[i]] = score
        
    return testResults     
        
        
def decode(x):
    
    results = testKeys(x)
    #On ordonne les keys du dictionnaire par score (croissant)
    sorted_results = sorted(results, key=results.__getitem__)
    print('Results in ascending order by score : ',sorted_results)
        
'''
SOLUTION 

decode('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736') 
-> "Cooking MC's like a pound of bacon", 88

'''