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



def toPNZ(stream,evenStream,amp):
    
    newStream=np.zeros((len(stream),evenStream))
    nullPart=np.zeros(evenStream/2)
#    para bit 1
    ampPartPosi=np.zeros(evenStream/2)
    ampPartPosi.fill(Amp)
    ones=np.hstack((ampPartPosi,nullPart))
#     para bit 0
    ampPartNega=np.zeros(evenStream/2)
    ampPartNega.fill(-Amp)
    zeros=np.hstack((ampPartNega,nullPart))
    
    for P in range(len(stream)):
        if(stream[P]==1):
            newStream[P]=ones
        else:
            newStream[P]=zeros
            
    return newStream.flatten()
    
#exercicio 2
lamba=0
pnzStream=toPNZ(Stream,even,Amp)   

    
def adaptedFilter(pnzStream,lambaDecisionValue):
    amp=0
    tbdiv2=0
    while(pnzStream[tbdiv2] != 0):
        amp+=abs(pnzStream[tbdiv2])
        tbdiv2=tbdiv2+1
        
    amp=int(round(amp/tbdiv2))
    
    return amp
    
    
    
    
#    for P in range(len(pnzStream)):
        
    
    
    
    
    
    
    