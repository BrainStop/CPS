# -*- coding: utf-8 -*-
"""
Created on Mon Dec 05 18:37:10 2016

@author: David
"""
import numpy as np


Stream= np.array([0,1,0,1,0,1,1,0])
even=6
Amp=5
#



def toPRZ(stream, evenStream, amp):
    newStream = np.zeros((len(stream), evenStream))
    indx_0 = np.where(stream[:,np.newaxis]==0)[0]
    indx_1 = np.where(stream[:,np.newaxis]==1)[0]
    newStream[indx_0,:evenStream/2] = amp
    newStream[indx_1,:evenStream/2] = -amp
    return newStream
#exercicio 2
lamba=0
pnzStream=toPRZ(Stream, even, Amp)


def adaptedFilter(przStream, even,lambaDecisionValue):
    prz_split = np.reshape(przStream, (-1, even))
    media = np.mean(prz_split, axis=1)
    return (media < lambaDecisionValue).astype(int)

def channelAWGN(signal_in, p_ruido):
    return sinal_in + np.sqrt(p_ruido) *  np.random.randn(len(sinal_in))
