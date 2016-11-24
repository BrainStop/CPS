# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 19:19:23 2016

@author: Administrator
"""

import sys
sys.path.append("../")
import numpy as np
#import matplotlib.pyplot as plt
#import scipy.io.wavfile as wav
#import trabalhoPratico02.trabalho_pratico02 as tp02
#import trabalhoPratico03.trabalho_pratico03 as tp03

I4 = np.identity(4)
P = np.array([[0, 1, 1], [1, 1, 0], [1, 0, 1], [1, 1, 1]])
G = np.hstack((I4, P))


I3 = np.identity(3)
H = np.vstack((P, I3))

m = np.array([0,1,0,1])

def codigo_hamming(m_bit_stream):
    bits_nx4 = np.reshape(m_bit_stream, (-1, 4))
    c_nx4 = np.dot(bits_nx4, G) % 2
    return c_nx4.flatten()

def detecao_correcao_erros(c_bit_stream):
    m = np.reshape(c_bit_stream, (-1, 7))
    s = np.dot(m, H) % 2
    for i in range(len(s)):
        error_index = np.where(np.all(H == s[i], axis=1))[0]
        if(error_index.size != 0):
            m[i, error_index[0]] = not bool(m[i, error_index[0]])
             
    return np.delete(m, [4,5,6], axis=1).flatten()

    
    
    
    
    
    
    
c = codigo_hamming(m)
erro = np.array([0, 1, 0, 1, 0, 0 ,0,
                 0, 1, 0, 1, 0, 1 ,1,
                 0, 1, 0, 1, 0, 0 ,1]) 


#erro = np.array([[0, 1, 0, 1], [0, 0 ,0], [0, 1, 0, 1, 0, 1 ,1, 0, 1, 0, 1, 0, 0 ,1]]) 
s = detecao_correcao_erros(erro)

#print( c.astype(int) )
#print( s.astype(int) )
#print(np.where(np.all(H == s, axis = 1)))