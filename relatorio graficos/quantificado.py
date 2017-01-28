# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 21:14:46 2017

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


fs = 80.0  # frequencia de amostragem
n = np.arange(0, 80)  # numero de amostras
fn = 20.0 * np.cos(2.0 * np.pi * n / fs)

nbits = 3
vmax = 20
vQ, vD = tp02.tabelas_mid_rise(nbits, vmax)
fq, fi, _, _ = tp02.quantificador(vQ, vD, fn)
plt.plot(fi, label="indices")
plt.plot(fq, label="amplitude")
plt.title("Conversor de indice para amplitude")
plt.grid(True)
plt.ylabel("Amplitude / Indice")
plt.xlabel("Amostra")
plt.legend()
plt.figure()
vMax = 20
fx = np.arange(-vMax, vMax + .5, 0.5)
nBits = 3

#print("fx", fx)
#print("Q", vQ)
#print("D", vD)
#fq, fi, _, _ = tp02.quantificador(vQ, vD, fx)
#print("fq", fq)
#print("fi", fi)
#plt.plot(fq, label="Quantificado")
#plt.plot(fx, label="Original")
#plt.title("Quantificador Midrise a 3 bits")
#plt.grid(True)
#plt.ylabel("Amplitude")
#plt.xlabel("Amostra")
#plt.legend()
