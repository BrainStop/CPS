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

<<<<<<< HEAD
I4 = np.identity(4)
P = np.array([[0, 1, 1], [1, 1, 0], [1, 0, 1], [1, 1, 1]])
=======
I4 = np.identity(4, dtype=bool)
P = np.array([[0, 1, 1], 
              [1, 1, 0], 
              [1, 0, 1],
              [1, 1, 1]], dtype=bool)
              
>>>>>>> origin/master
G = np.hstack((I4, P))


<<<<<<< HEAD
I3 = np.identity(3)
H = np.vstack((P, I3))

m = np.array([0,1,0,1])

def codigo_hamming(m_bit_stream):
    bits_nx4 = np.reshape(m_bit_stream, (-1, 4))
    c_nx4 = np.dot(bits_nx4, G) % 2
=======
def codigo_hamming(bit_stream):
#    falta acrescentar zeros caso o array nao seja multiplo de 4
    bits_nx4 = np.reshape(bit_stream, (-1, 4))
    c_nx4 = np.dot(bits_nx4, G)
>>>>>>> origin/master
    return c_nx4.flatten()
    
codedArray=codigo_hamming(m1)
    
    
#tentei mas sem sucesso
def errorCorrection(bitStream):
#""" transformar em array bidimensional de 7 em 7"""
    bits_nx7 = np.reshape(bitStream, (-1, 7))
    print(bits_nx7)
    bits_nx7=bits_nx7.astype(np.int16)
    print(bits_nx7)
#    para cada 7
    for i in range(len(bits_nx7)):
#        if
#        inicializar array para saber o bit em erro
        packbitsArray=np.zeros((3),dtype=np.uint8)
#        %2==a xor
        parity0=sum(bits_nx7[i][1]+bits_nx7[i][2]+bits_nx7[i][3])%2 
        parity1=sum(bits_nx7[i][0]+bits_nx7[i][1]+bits_nx7[i][3])%2
        parity2=sum(bits_nx7[i][0]+bits_nx7[i][2]+bits_nx7[i][3])%2
        packbitsArray[0]=parity0
        packbitsArray[1]=parity1
        packbitsArray[2]=parity2
        print(packbitsArray)
#        de bits para decimal indice do bit em erro
        bitInError=np.packbits(packbitsArray)
#        bitInError dame 32 nao percebo porque!
        print(bitInError)
#   TODO     corrigir bit posicao bitINError 32 é um numero errado 001 devia dar 1 int e esta a dar 32????
        if bits_nx7[i][bitInError]==0:
            bits_nx7[bitInError]=1
        else:
            bits_nx7[bitInError]=0
    return bits_nx7.flatten().astype(np.bool)
correctedArray=errorCorrection(codedArray)
    

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