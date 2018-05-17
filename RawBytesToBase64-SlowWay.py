#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 00:47:21 2017

@author: Razorin
"""

import re
import math
import base64
import array

#Convert each hex digit in binary digits
def hexToBinary(hexList):
    
    binList = []

    for i in hexList:

        #Convert hex letter in decimal digits
        if re.match('[a-f]', i):
            if i == 'a':
                r = 10
            elif i == 'b':
                r = 11
            elif i == 'c':
                r = 12
            elif i == 'd':
                r = 13
            elif i == 'e':
                r = 14
            elif i == 'f':
                r = 15         
        else:    
            r = int(i)
    
        #Convert into binary digits by group of 4
        for k in range(4):
            if r // (math.pow(2,(3-k))) > 0:             
                binList.append(1)      
                r = r % (math.pow(2,(3-k)))
            else:
                binList.append(0)
    
    return binList


#Group bits in 8-bits bytes
def bitsToBytes(bits):
    
    h = len(bits) // 8
    Bytes = [ 0 for i in range(h)]
    k = 0
    
    while k < len(bits):
        for u in range(h):
            for i in range(8):
                Bytes[u] =  str(Bytes[u]) + str(bits[i + (8*u)])
                k = k + 1
    return Bytes


def base2ToBase10(base2):
    
    base10 = 0
    k = 1
    
    for i in base2 :
        base10 = int(base10 + (int(i) * math.pow(2, len(base2) - k)))
        k = k + 1
        
    return base10


#Rewrite the 8-bits Bytes in decimal
def bytesRewrite(Bytes):
    
    result = []
    
    for i in range(len(Bytes)):
       result.append(base2ToBase10(Bytes[i]))
       
    return result


#Encode 8-bits Bytes in Base64
def bytesToBase64(Bytes):
  
    for i in range(len(Bytes)) :
        Bytes[i] = int(Bytes[i])
        
    result = base64.b64encode(array.array('B', Bytes))
    
    return result


#Get them all together
def hexToBase64(hexa):
    
    print()
    print('hexToBinary(hexa) : ', hexToBinary(hexa))
    print()
    print('bitsToBytes(hexToBinary(hexa)) :' , bitsToBytes(hexToBinary(hexa)) )
    print()
    print('bytesRewrite(bitsToBytes(hexToBinary(hexa)))', bytesRewrite(bitsToBytes(hexToBinary(hexa))))
    print()
    print('-'*20)
    print('bytesToBase64(bytesRewrite(bitsToBytes(hexToBinary(hexa)))) :')
    print()
    result = bytesToBase64(bytesRewrite(bitsToBytes(hexToBinary(hexa))))
   
    return result




