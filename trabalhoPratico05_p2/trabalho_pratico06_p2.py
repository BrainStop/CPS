# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 16:16:58 2017

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

def QPSK(bits, Eb, P=8):
    
    n = np.arange(P) #Amostras por simbolo
    A = np.sqrt(Eb * 2 / P) #Amplitude de cada simbolo
    
    #Sinal de cada Simbolo
    simbolo_11 = A * np.cos(2 * np.pi * n/P - (np.pi/4))
    simbolo_01 = A * np.cos(2 * np.pi * n/P - (3*np.pi/4))
    simbolo_00 = A * np.cos(2 * np.pi * n/P - (5*np.pi/4))
    simbolo_10 = A * np.cos(2 * np.pi * n/P - (7*np.pi/4))

    bitsReshape = bits.reshape((-1,2))
    resultado = np.zeros((len(bits)/2,P))
    
    resultado[np.all(bitsReshape == [0,0], axis=1)] = simbolo_00
    resultado[np.all(bitsReshape == [0,1], axis=1)] = simbolo_01
    resultado[np.all(bitsReshape == [1,0], axis=1)] = simbolo_10
    resultado[np.all(bitsReshape == [1,1], axis=1)] = simbolo_11

    return resultado.flatten()
    
def receptor(simbolos, P=8):
    n = np.arange(P)
    simbolos_r = simbolos.reshape((-1, P))
    vx = np.sqrt(2. / P) * np.cos(2. * np.pi * n / P)
    vy = np.sqrt(2. / P) * np.sin(2. * np.pi * n / P)
    vxy = np.vstack((np.dot(simbolos_r, vx) , np.dot(simbolos_r, vy))).T
    bits = (vxy > 0).flatten()
    return bits.astype(int)

bits = np.array([0,0,0,1,1,0,1,1])
print "enviado ", bits
s = QPSK(bits, 64)
c = receptor(s)
print "recebido", c