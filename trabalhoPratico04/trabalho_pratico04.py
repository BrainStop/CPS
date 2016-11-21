# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 19:19:23 2016

@author: Administrator
"""

import sys
sys.path.append("../")
import numpy as np
#import matplotlib.pyplot as plt
#import scipy.io.wavfile as wav
#import trabalhoPratico02.trabalho_pratico02 as tp02
#import trabalhoPratico03.trabalho_pratico03 as tp03

I4 = np.identity(4, dtype=bool)
P = np.array([[0, 1, 1], [1, 1, 0], [1, 0, 1], [1, 1, 1]], dtype=bool)
G = np.hstack((I4, P))

m1 = np.array([0,1,0,1,1,0,1,0,1,0,0,1,0,1,0,1], dtype=bool)

def codigo_hamming(bit_stream):
    bits_nx4 = np.reshape(bit_stream, (-1, 4))
    c_nx4 = np.dot(bits_nx4, G)
    return c_nx4.flatten()


print(len(codigo_hamming(m1)))