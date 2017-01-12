# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 16:08:53 2016

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

def tabelas_mid_rise(nBits, vMax):
    """Cria as tabelas de valores de quantificacao e decisao utilizadas para a 
    codificacao

    Parameters
    ----------
    nBits : Integer define o numero de bits que serao usados para quantificacao
    vMax : Integer define a amplitude maxima que o sinal a codificar tem
    
    Returns
    -------
    out : tuplo com um ndarray 1D com os valores de quantificacao e um  ndarray
    1D com os valores de decisao
 
    Examples
    --------
    >>> tabelas_mid_rise(4, 5)
    (array([-4.6875, -4.0625, -3.4375, ...,  3.4375,  4.0625,  4.6875]),
    array([-4.375, -3.75 , -3.125, ...,  3.125,  3.75 ,  4.375]))
    """
    delta = 2.0 * vMax / 2.0**nBits
    vQ = np.arange(-vMax + delta / 2.0, vMax, delta)
    vD = np.arange(-vMax + delta, vMax - delta / 2.0, delta)
    return vQ, vD

def quantificador(vQ, vD, fx):
    """Quantifica um sinal usando as tabelas de quantificacao e decisao 
    introduzidas

    Parameters
    ----------
    vQ : ndarray 1D com os valores de quantificacao
    vD : ndarray 1D com os valores de decisao
    fx : ndarray 1D com o sinal a quantificar
    
    Returns
    -------
    out : tuplo com um ndarray 1D com o sinal quantificado e um ndarrau 1D com 
    os indices referentes aos valores quantificados da tabela de quantificacao
 
    Notes
    -------
    Se forem introduzidas tabelas com valores de quantificados que nao sejam 
    adequados a funcao gera novas tabelas de quantificacao e decisao
    
    Examples
    --------
    >>> vQ, vD = tabelas_mid_rise(4, 5)
    >>> quantificador(vQ, vD, np.arange(-5, 6))
    """
    vMaxp = np.max(fx) # Amplitude maxima do sinal fx
    vMaxn = np.min(fx) # Amplitude minima do sinal fx
    meioDelta = np.abs(vQ[0] - vQ[1]) / 2
    
    # Condição que veririfica se ambas as aplitudes estão contidas no vQ
    if(vMaxp > vQ[-1] + meioDelta or vMaxn < vQ[0] - meioDelta):
        if(vMaxp > np.abs(vMaxn)):
            vQ, vD = tabelas_mid_rise(np.log2(len(vQ)), vMaxp)
        else:
            vQ, vD = tabelas_mid_rise(np.log2(len(vQ)), np.abs(vMaxn))

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
    return (fq, fi, vQ, vD)  

def tabelas_mid_tread(nBits, vMax):
    delta = 2. * vMax / 2.**nBits
    quantificacionValues = np.arange(-vMax + (delta), vMax + delta, delta)
    decisionValues = np.arange(-vMax + (delta), vMax + (delta - (delta / 2)), delta)
    return quantificacionValues, decisionValues, delta

def sne(signalIn, R, vMax):
    vMax = np.max(signalIn)
    quanti, deci = tabelas_mid_rise(R, vMax)
    signalOut, used = quantificador(signalIn, quanti, deci)
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
    vQ, vD = tabelas_mid_rise(nBits, vMax)
    print("fx", fx)
    print("Q", vQ)
    print("D", vD)
    fq, fi = quantificador(vQ, vD, fx)
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
        vQ, vD = tabelas_mid_rise(R[i], vMax)
        print("fx", fx)
        print("Q", vQ)
        print("D", vD)
        fq, fi = quantificador(vQ, vD, fx)
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
