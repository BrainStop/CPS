# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 16:08:53 2016

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav


def TabelasMidRise(nBits, vMax):
    delta = 2.*vMax / 2.**nBits
    vQ = np.arange(-vMax+delta/2., vMax, delta)
    vD = np.arange(-vMax + delta, vMax - delta/2, delta)
    return vQ, vD

def Quantificador(vQ, vD, fx):
    vMaxp = np.max(fx) # Amplitude maxima do sinal fx
    vMaxn = np.min(fx) # Amplitude minima do sinal fx
    meioDelta = np.abs(vQ[0] - vQ[1]) / 2
    
    # Condição que veririfica se ambas as aplitudes estão contidas no vQ
    if(vMaxp > vQ[-1] + meioDelta or vMaxn < vQ[0] - meioDelta):
        if(vMaxp > np.abs(vMaxn)):
            vQ, vD = TabelasMidRise(np.log2(len(vQ)), vMaxp)
        else:
            vQ, vD = TabelasMidRise(np.log2(len(vQ)), np.abs(vMaxn))

    # Array de valores quantificados
    fq = np.ones(len(fx), dtype=float) * vQ[-1]
    # Array dos idices da tabela de quantificação referentes aos valores quantificados
    fi = np.ones(len(fx), dtype=float) * len(vQ) - 1
    for i in range(len(fx)):
        arrayBin = fx[i] <= vD
        arrTrue = np.where(arrayBin == True)[0]
        if(len(arrTrue) > 0):
            fq[i] = vQ[arrTrue[0]]
            fi[i] = arrTrue[0]
    return fq, fi  

def tabelasmidtread(nBits, vMax):
    delta = 2. * vMax / 2.**nBits
    quantificacionValues = np.arange(-vMax + (delta), vMax + delta, delta)
    decisionValues = np.arange(-vMax + (delta), vMax + (delta - (delta / 2)), delta)
    return quantificacionValues, decisionValues, delta

def SNR(signalIn, R, vMax):
    vMax = np.max(signalIn)
    quanti, deci = TabelasMidRise(R, vMax)
    signalOut, used = Quantificador(signalIn, quanti, deci)
    Px = np.sum([(signalIn**2) / 2])
    PRuido = vMax**2 / (3 * (2**(2 * R)))
    SNRT = 6. * R + 10. * np.log10((3. * Px) / (vMax**2))
    SNRP = 10. * np.log10(Px / PRuido)
    return SNRT, SNRP
    
def main():
    # exercicio 3
    # a)
    vMax = 20
    fx = np.arange(-vMax, vMax + .5, 0.5)
    nBits = 3
    vQ, vD = TabelasMidRise(nBits, vMax)
    print("fx", fx)
    print("Q", vQ)
    print("D", vD)
    fq, fi = Quantificador(vQ, vD, fx)
    print("fq", fq)
    print("fi", fi)
    plt.plot(fq)
    plt.plot(fx)
    
    # b)
    eq = fx - fq
    plt.figure()
    plt.plot(eq)
    plt.figure()
    hx, b = np.histogram(eq, 10)
    plt.bar(b[:-1], hx, width=.20 , color=[.9, .9, .9])
    
    # c)
    vMax = 20.
    fx = np.arange(-vMax, vMax + .5, 0.5)
    p = sum(fx * fx) / len(fx)
    R = np.arange(3,9,1)
    SNRT = np.arange(len(R), dtype='float')
    SNRP = np.arange(len(R), dtype='float')
    
    for i in range(len(R)):
        vQ, vD = TabelasMidRise(R[i], vMax)
        print("fx", fx)
        print("Q", vQ)
        print("D", vD)
        fq, fi = Quantificador(vQ, vD, fx)
        print("fq", fq)
        print("fi", fi)
        plt.figure()
        plt.plot(fq)
        plt.plot(fx)
        eq = fx - fq
        peq =  sum(eq * eq) / len(eq)
        SNRT[i] = 6. * R[i] + 10. * np.log10((3. * p) / (vMax**2))
        SNRP[i] = 10. * np.log10(p/peq)
        
    plt.figure()
    plt.plot(R, SNRT)
    plt.plot(R, SNRP)
    
    # exercicio 4
    # a)
    #rate, data = wav.read("D:/LEIM/3_Semestre/CPS/pythonWorkspace_1617/wavFiles/guitarra.wav", "r")
