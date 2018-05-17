#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 19:42:29 2017

@author: Razorin
"""

from challenge1FinalAuto import hexToBytes

x = '1c0111001f010100061a024b53535009181c'
y = '686974207468652062756c6c277320657965'

def xorHexas(x, y):
    
   x = hexToBytes(x)
   y = hexToBytes(y)
   
   xBin = ''
   yBin = ''
   
   for i in range( len(x) ):
       xBin = str(xBin) + str('0'* (8 - (len(bin(x[i]) [2:])))) + str( bin(x[i]) [2:] )

   for i in range( len(y) ):
       yBin = str(yBin) + str('0'* (8 - (len(bin(y[i]) [2:])))) + str( bin(y[i]) [2:] )
   
   xor = ''
   
   for i in range( len(xBin) ):
 
       if xBin[i] == yBin[i]:
           xor = xor + '0'
       else:
           xor = xor + '1'
           
   xor = hex(int(xor, 2))[2:]
   
   return xor 

print(xorHexas(x, y))