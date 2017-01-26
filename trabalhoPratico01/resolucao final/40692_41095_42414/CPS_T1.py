# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import scipy.signal as ss

# from soundPlay import soundPlay

# fechar as anteriores
plt.close('all')



# variaveis
fs = 8000
angle = 20000
freq = 3014.0
duration = 1.
n = np.arange(fs*duration)   
pi2 = np.pi * 2
x = angle*np.cos(pi2 * freq * n / fs)


#==============================================================================
# ex)1 
#•plot"
def ex1plots(x):
    #Graficos
    wav.write("primeiroSom_ex1.wav",fs,x.astype('int16'))
    plt.figure('Grafico0',facecolor = 'w',figsize=(15,8))
    plt.title("Ex1 Sinusoide")
    plt.plot(1.0*n/fs,x)#1.0 para ser float!
    plt.axis([0,5./8000,-angle,angle])  # alterar os eixos para conterem apenas 5 periodos do sinal

#ex1plots(x)

def ex1fft(x):
    #fft da numeros complexos
    X=np.fft.fft(x)/len(x)
    plt.plot(1.0*n,X)
    FREQ=np.fft.fftfreq(len(X))*fs #fs normalizar freq.
    #grafico fft
    plt.figure('Grafico1',facecolor = 'w',figsize=(15,8))
    plt.title("Ex1 FFT da Sinusoide")
    plt.plot(FREQ,np.abs(X))
    plt.grid(True)
#ex1fft(x)
    
def ex1fftshift(x):
    X=np.fft.fftshift(x)/len(x)
    plt.plot(1.0*n,X)
    FREQ=np.fft.fftfreq(len(X))*fs #fs normalizar freq.
    #grafico fft
    plt.figure('Grafico2',facecolor = 'w',figsize=(15,8))
    plt.title("Ex1 FFTshift da Sinusoide")
    plt.plot(FREQ,np.abs(X))
    plt.grid(True)
#ex1fftshift(x)

rate,data=wav.read('guitarra.wav','r')

#def ex1som_b():
#    #Ler ficheiro e ver quais as frequencias
#    rate,data=wav.read("guitarra.wav")
#    print(rate)
#    #grafico
#    plt.figure('Grafico3',facecolor = 'w',figsize=(15,8))
#    plt.title("Ex1 Representacao Grafica do Som Guitarra")
#    plt.plot(np.arange(len(data)),data)
#    plt.grid(True)
#    
#    X=np.fft.fft(data)/len(data)
#    XFREQ=np.fft.fftfreq(len(data))*fs #normalizar freq.
#    plt.figure('Grafico4',facecolor = 'w',figsize=(15,8))
#    plt.title("Ex1 FFt Som Ficheiro Guitarra")
#    plt.plot(XFREQ,np.abs(X))
    
def ex1som_b():
    #Ler ficheiro e ver quais as frequencias
    rate,data=wav.read("guitarra.wav")
    print(len(data))
    print(rate)
    
    #grafico
    plt.figure('Grafico3',facecolor = 'w',figsize=(15,8))
    plt.title("Ex1 Representacao Grafica do Som Guitarra")
    plt.plot(np.arange(len(data)),data)
    plt.grid(True)
    
    dataAmostrado=data[::3.15] #441000 amostras
    print(len(dataAmostrado))
    dataAmostrado=dataAmostrado[0:44100]
    wav.write("guitarraAmostrado44100.wav",rate,dataAmostrado.astype('int16'))
    #grafico
    plt.figure('Grafico20',facecolor = 'w',figsize=(15,8))
    plt.title("Ex1 Representacao Grafica do Som Guitarra a 44100Hz")
    plt.plot(np.arange(len(dataAmostrado)),dataAmostrado)
    plt.grid(True)
    
    X=np.fft.fft(data)
    XFREQ=np.fft.fftfreq(len(data))*len(data) #normalizar freq.
    plt.figure('Grafico4',facecolor = 'w',figsize=(15,8))
    plt.title("Ex1 FFt Som Ficheiro Guitarra original")
    plt.plot(XFREQ,np.abs(X))
    
    X=np.fft.fft(dataAmostrado)
    XFREQ=np.fft.fftfreq(len(dataAmostrado))*len(dataAmostrado) #normalizar freq.
    plt.figure('Grafico50',facecolor = 'w',figsize=(15,8))
    plt.title("Ex1 FFt Som Ficheiro Guitarra Amostrado a 44100Hz")
    plt.plot(XFREQ,np.abs(X))
   
    
ex1som_b()
#==============================================================================
#==============================================================================
# ex2)
def ex2som_a():
    #Ler ficheiro e ver quais as frequencias
    rate,data=wav.read("guitarra.wav")
    fs4000Hz=data[::34]#amostragem a 4000
    fs4000Hz=fs4000Hz[0:4000]
    #grafico
    plt.figure('Grafico66',facecolor = 'w',figsize=(15,8))
    plt.title("Ex2 Representacao Grafica do Som Guitarra a 4000Hz")
    plt.plot(np.arange(len(fs4000Hz)),fs4000Hz)
    plt.grid(True)
    
    X=np.fft.fft(fs4000Hz)/len(fs4000Hz)
    XFREQ=np.fft.fftfreq(len(fs4000Hz))*4000 #normalizar freq.
    plt.figure('Grafico5',facecolor = 'w',figsize=(15,8))
    plt.title("Ex2 FFT Ficheiro Guitarra Amostrado a 4000Hz")
    plt.plot(XFREQ,np.abs(X))
    wav.write("guitarraAmostrado4000.wav",rate,fs4000Hz.astype('int16'))
#    soundPlay(fs4000Hz,4000)
ex2som_a()

def ex2som_b():
    #Ler ficheiro e ver quais as frequencias
    rate,data=wav.read("guitarra.wav")
    
    fs1000Hz=data[::139]#amostragem a 1000 amostras
    fs1000Hz=fs1000Hz[0:1000]
    #grafico
    plt.figure('Grafico65',facecolor = 'w',figsize=(15,8))
    plt.title("Ex2 Representacao Grafica do Som Guitarra a 1000Hz")
    plt.plot(np.arange(len(fs1000Hz)),fs1000Hz)
    plt.grid(True)
    
    
    X=np.fft.fft(fs1000Hz)/len(fs1000Hz) #fft
    XFREQ=np.fft.fftfreq(len(fs1000Hz))*1000 #normalizar freq.
    plt.figure('Grafico6',facecolor = 'w',figsize=(15,8))
    plt.title("Ex2 FFT Ficheiro Guitarra Amostrado a 1000Hz")
    plt.plot(XFREQ,np.abs(X))
    wav.write("guitarraAmostrado1000.wav",rate,fs1000Hz.astype('int16'))
#    soundPlay(fs1000Hz,1000)
ex2som_b()

fAmostragem=44000
n=np.arange(fAmostragem)
signal=4*np.cos(pi2*10000*n)+10*np.cos(pi2*25000*n)
#==============================================================================
#==============================================================================
# ex3)
#o 3 nao ficou finalizado em python, encontrasse finalizado em pdf
def ex3_a(signalIN):
    Fc1=20000.0 #frequencia de corte
    lowPassFilter=ss.firwin(Fc1,1/Fc1,scale=True);
    X=np.fft.fft(signalIN)
    XFREQ=np.fft.fftfreq(signalIN.size)
    plt.figure('Grafico7',facecolor = 'w',figsize=(15,8))
    plt.title("freqs")
    plt.plot(XFREQ,np.abs(X))
    
    newX=np.convolve(lowPassFilter,X)
    newXFREQ=np.fft.fftfreq(len(newX))*fAmostragem
    plt.figure('Grafico8',facecolor = 'w',figsize=(15,8))
    plt.title("Com aliasing")
    plt.plot(newXFREQ,np.abs(newX))
    
#ex3_a(signal)
    


def ex3_b(signalIN):
    Fc1=30000.0 #frequencia de corte
    lowPassFilter=ss.firwin(fAmostragem,1/Fc1);
    X=np.fft.fft(signalIN)/len(signalIN)
    XFREQ=np.fft.fftfreq(len(signalIN))*fs
    plt.figure('Grafico9',facecolor = 'w',figsize=(15,8))
    plt.title("freqs")
    plt.plot(XFREQ,np.abs(X))
    
    newX=ss.fftconvolve(lowPassFilter,X)
    newXFREQ=np.fft.fftfreq(len(newX))*fs
    print(newX)
    plt.figure('Grafico10',facecolor = 'w',figsize=(15,8))
    plt.title("Com aliasing")
    plt.plot(newXFREQ,np.abs(newX))  
    
#ex3_b(x)

#==============================================================================

