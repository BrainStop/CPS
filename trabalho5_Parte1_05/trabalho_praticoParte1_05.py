# -*- coding: utf-8 -*-
"""
Created on Mon Dec 05 18:37:10 2016

@author: David
"""
import numpy as np
import matplotlib.pyplot as plt

Stream= np.array([0,1,0,1,0,1,1,0])
even=6
Amp=5

def toPRZ(stream, evenStream, amp):
    newStream = np.zeros((len(stream), evenStream))
    indx_0 = np.where(stream[:,np.newaxis]==0)[0]
    indx_1 = np.where(stream[:,np.newaxis]==1)[0]
    newStream[indx_0,:evenStream/2] = amp
    newStream[indx_1,:evenStream/2] = -amp
    return newStream.flatten()
    
#exercicio 2
lamba=0
pnzStream=toPRZ(Stream, even, Amp)

def adaptedFilter(przStream, even,lambaDecisionValue):
    prz_split = np.reshape(przStream, (-1, even))
    media = np.mean(prz_split, axis=1)
    return (media < lambaDecisionValue).astype(int)


def channelAWGN(signal_in, p_noise):
#    noise é a varianca
    return signal_in + (np.sqrt(p_noise)*np.random.randn(len(signal_in)))
    

def ex4TestesAsFuncAnteriores():
#    alinea a)

#   PRZ vals
    stremTest=np.array([0,1,1,0,0,1])
    P=8
    A=1
    przStreamTest=toPRZ(stremTest,P,A)
#    ruido acrescentar no sinal
    noise=1
#    limiar decisao
    limiar=0
#    sinal PRZ com ruido
    przStremWhitNoise=channelAWGN(przStreamTest,noise)
#   Represente o sinal à entrada e à saída do canal.
    plt.figure('Grafico0',facecolor = 'w',figsize=(15,8))
    plt.title("Comparacao entre sinal a entrada e a saida o canal AWGN")
    plt.plot(przStreamTest)
    plt.plot(przStremWhitNoise)
    
#    sinal sem ser codificado
    stremTest=np.array([0,1,1,0,0,1]) 
#    sinal codificado e descodificado com ruido
    descodiPrzStremWhitNoise=adaptedFilter(przStremWhitNoise,P,limiar)
#    output:
#           array([1, 1, 1, 0, 0, 0]) existe erro
    
#    alinea b)
    varianVals=np.array([0.5,1,2])
    for i in range(len(varianVals)):#melhorar esta cena
        przStremWhitNoise=channelAWGN(przStreamTest,varianVals[i])
        plt.figure("Grafico"+str(i+1),facecolor = 'w',figsize=(15,8))
        plt.title("Comparacao entre sinal a entrada e a saida o canal AWGN com variancia "+str(varianVals[i]))
        plt.plot(przStreamTest)
        plt.plot(przStremWhitNoise)
#        com o aumento da variancia(ruido) o sinal 
#        começa a ser muito diferente do original
        
    

#TODO começar o ex5
    
    
    
    
    