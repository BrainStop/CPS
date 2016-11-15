# -*- coding: latin1 -*-
#Entradas: x: numpy array 
#         Fs: frequência de amostragem (int16)
import pyaudio 
import numpy as  np
def soundPlay(x,Fs):
    Fs=np.int64(Fs)
    x=np.array(x,'float32')           #converter para float
    x=x-x.mean(); x=x/np.abs(x).max() #tirar média, escalar
    x=np.int16(np.round(x*(2**15-1))) #converter para int16bits
    xI=x.tostring()   #converter x para binary string 
    auPort=pyaudio.PyAudio()  #instanciar audio
    auStream=auPort.open(format=8,channels=1,rate=Fs,output=True)
    auStream.write(xI)        #play x
    auStream.stop_stream()    # stop stream 
    auPort.terminate()        # close PyAudio 