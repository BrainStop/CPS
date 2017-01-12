# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 16:16:58 2017

@author: Administrator
"""

import sys
sys.path.append("../")

import trabalhoPratico02.trabalho_pratico02 as tp02
import trabalhoPratico03.trabalho_pratico03 as tp03
import trabalhoPratico04.trabalho_pratico04 as tp04
import trabalhoPratico05_p1.trabalho_pratico05_p1 as tp05p1

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

def qpsk(bits, Eb, P=8):
    
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
    
def decode_qpsk(simbolos, P=8):
    n = np.arange(P)
    simbolos_r = simbolos.reshape((-1, P))
    vx = np.sqrt(2. / P) * np.cos(2. * np.pi * n / P)
    vy = np.sqrt(2. / P) * np.sin(2. * np.pi * n / P)
    vxy = np.vstack((np.dot(simbolos_r, vx) , np.dot(simbolos_r, vy))).T
    bits = (vxy > 0).flatten()
    return bits.astype(int)

def main():
#    filepath = "C:/cenas do disco/LEIM/3_Semestre/CPS/wavFiles/guitarra.wav"
#    _, data = wav.read(filepath)
    
    data = np.array([8,7,-2,-7,9,-10])
#    print "data", data

    #numero de bits da codificacao
    nbits = 4
#    print "nbits", bits
    
    if(np.max(data) > np.abs(np.min(data))):
        vQ, vD = tp02.TabelasMidRise(nbits, np.max(data))
    else:
        vQ, vD = tp02.TabelasMidRise(nbits, np.abs(np.min(data)))
        
    
#    print "vD", vD
        
    #Quantificador
    valQuanti, valIndices = tp02.Quantificador(vQ, vD, data)
    print "vQ", valQuanti
#    print valIndices
    
    #Codificacao
    codeVals = tp03.codificacao(nbits, valIndices)
    
    #Codificacao de Hamming
    codeHamming = tp04.codificacao_hamming(codeVals)
    
    #code QPSK
    codeQPSK = qpsk(codeHamming, 64)
    
    #canal ruido
    noise = 1
    code_noise = tp05p1.channel_awgn(codeQPSK, noise)
    
    print sum( codeQPSK != code_noise )
    plt.plot(codeQPSK[0:15])
#    plt.plot(code_noise[0:15])
    
    #Decode QPSK
    decodeQPSK = decode_qpsk(code_noise)
    
    #Decode Hamming
    decodeHamming = tp04.descodificacao_hamming(decodeQPSK)
    
    #Decode bits
    decodeBits = tp03.descodificacao(nbits, decodeHamming)
    
    print "final", vQ[decodeBits]
    print sum(vQ[decodeBits] != valQuanti)
    
    
main();
    
    
    
    
    
    
    
    
    
    
    
    