# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 16:05:46 2016

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

#x(t) = 2000 * cos(2pi * 3014 * t) funcao do sinal continuo

fs = 8000.0 #frequencia de amostragem
n = np.arange(0,8000) #numero de amostras
fn = 20000.0 * np.cos(2.0 * np.pi * 3014.0 * n / fs) # funçao discreta do sinal

wav.write("sinusoide_ex1a.wav", fs, fn.astype('int16')) # gravar a sinusoide

# conversao de amostras para tempo n/fs
#plt.figure()
#plt.plot(n/fs, fn) # representacao do sinal em funcao do tempo
#plt.axis([0, 5.0/fs, -20000, 20000]) # alterar os eixos para conterem apenas 5 periodos do sinal

X = np.fft.fft(fn)/len(fn) #dividimos por len(x) para termos a amplitude correcta
#plt.figure()
#plt.plot(np.abs(X))
freq = np.fft.fftfreq(len(fn)) * fs # funcao devolve a frequencia normalizada ([-0.5, 0.5]) e entao multiplicamos por fs
#plt.figure()
#plt.plot(freq, np.abs(X))


rate, data = wav.read("D:/LEIM/3_Semestre/CPS/pythonWorkspace_1617/wavFiles/furelise.wav", "r")
#plt.figure()    
#plt.plot(data)
X = np.fft.fft(data)/len(data)
freq = np.fft.fftfreq(len(data)) * rate * 1.0
#plt.figure()
#plt.plot(freq, np.abs(X))

fn4khz = fn[::2]
wav.write("sinusoide_ex2a.wav", 4000, fn4khz.astype('int16'))
#
plt.figure()
plt.plot(np.arange(0,4000)/4000.0, fn4khz)
plt.plot(n/fs, fn)
plt.axis([0, 5.0/fs, -20000, 20000]) # alterar os eixos para conterem apenas 5 periodos do sinal

    
    
    