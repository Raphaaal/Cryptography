#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 00:43:40 2017

@author: Razorin
"""

import base64

def hexToBytes(hexa):
    
    b = bytes.fromhex(hexa)
    
    return b



def bytesToBase64(b):
    
   b = base64.b64encode(b)
   
   return b 
    

    
def hexToBase64(hexa):
    
    result = bytesToBase64(hexToBytes(hexa))
    
    return result