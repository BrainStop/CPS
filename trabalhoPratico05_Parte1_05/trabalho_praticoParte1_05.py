# -*- coding: utf-8 -*-
"""
Created on Mon Dec 05 18:37:10 2016

@author: David
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import math

import sys
sys.path.append("../")

import trabalhoPratico02.trabalho_pratico02 as tp02
import trabalhoPratico03.trabalho_pratico03 as tp03
import trabalhoPratico04.trabalho_pratico04 as tp04


Stream= np.array([0,1,0,1,0,1,1,0])
even=6
Amp=5

#Modulacao digital
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

def decodePRZ(przStream, even,lambaDecisionValue):
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
#   sinal sem ser codificado
    stremTest=np.array([0,1,1,0,0,1]) 
#    sinal codificado e descodificado com ruido
    descodiPrzStremWhitNoise=decodePRZ(przStremWhitNoise,P,limiar)
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
        
def toString(info,val):
    print(str(info)+str(val))

def ex5testeATodoSistema():
#    Ler ficheiro e ver quais as frequencias
#    carregar ficheiro
#
#original
    sys.path.append("cd")
    rate, data = wav.read("guitarra.wav")
    toString("Data: ", data)

#    tabela MidRise
    vQ,vD=tp02.TabelasMidRise(4,np.max(data))
#    toString("valor Quantificacao:",vQ)
#    toString("valor Decisao:",vD)
    
#    quantificaçao do ficheiro pela tabela MidRise    
    valQuanti, valIndices=tp02.Quantificador(vQ,vD,data)
#    toString("Data Quantificado:",valQuanti)
    toString("Data Indices:",valIndices)
    
#    codificacao
    codiVals=tp03.codificacao(4,valIndices)
    toString("CodiVals: ", codiVals)
    toString("CodiValsSHAPE:", codiVals.shape)    
#    codificacao em Hamming
    codeHamming=tp04.codificacao_hamming(codiVals)
    toString("CodeHamming: ", codeHamming)
    toString("CodeHammingSHAPE: ", codeHamming.shape)
#    Modulaçao Digital
    codePRZ=toPRZ(codeHamming,8,1)
    toString("CodePRZ: ", codePRZ)
    
#    adiciona ruido
    noise = np.array([0.5, 1, 2, 4])
    for n in noise:
        afterPassChannelAWGN=channelAWGN(codePRZ, n)
        toString("Ruido: ", n)
        toString("CANALRUIDO: ", afterPassChannelAWGN)
        toString("DIFERENCAS: ", np.sum(afterPassChannelAWGN!=codePRZ))
        
    #    passa de modulacao sinal para binario
        decodeprz=decodePRZ(afterPassChannelAWGN,2,0)
        toString("DecodePRZ: ",decodeprz)
        toString("DIFERENCAS: ", np.sum(decodeprz!=codeHamming))
        
    #    descodificacao Hamming
        decodeHamming=tp04.descodificacao_hamming(decodeprz)
        toString("decodeHamming: ", decodeHamming)
        toString("DIFERENCAS: ", np.sum(decodeHamming!=codiVals))
        
    #    descodificacao de binario
        decodeBits=tp03.descodificacao(4,decodeHamming)
        toString("decodeBits", decodeBits)
        toString("DIFERENCAS: ", np.sum(decodeBits!=valIndices))
        
        p = sum(data * data) / len(data)
        eq = data - valQuanti
        peq =  sum(eq * eq) / len(eq)
        SNRP = 10. * np.log10(p/peq)
        
        BERP = data / np.sum(decodeBits!=valIndices)
        BERT = 0.5 * math.erfc(math.sqrt((3*3/n)))
        
        toString("BERT", BERT)
        toString("BERP", BERP)
        toString("SNRP", SNRP)