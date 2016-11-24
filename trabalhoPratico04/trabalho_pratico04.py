# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 19:19:23 2016

@author: Administrator
"""

import sys
sys.path.append("../")
import numpy as np
import copy
#import matplotlib.pyplot as plt
#import scipy.io.wavfile as wav
#import trabalhoPratico02.trabalho_pratico02 as tp02
#import trabalhoPratico03.trabalho_pratico03 as tp03

#criacao da matriz geradora de identidade
# matriz identidade k = 4
I4 = np.identity(4)
# sub-matriz geradora de paridade
P = np.array([[0, 1, 1], 
              [1, 1, 0], 
              [1, 0, 1],
              [1, 1, 1]])
# matriz geradora de hamming k*q = 4*7
G = np.hstack((I4, P))

# criação da matriz sindroma
# matriz idendidade k = 3
I3 = np.identity(3)
# sindroma n*q = 7*4
H = np.vstack((P, I3))

def codificacao_hamming(m_stream):
    """Codifica um array binario de N mensagens utilizando a 
        codificacao de hammming

    Parameters
    ----------
    m_stream : ndarray 1D de N bits onde serão aplicados a 
        codificacao de hamming.

    Returns
    -------
    c_stream : ndarray 1D da mensagem com a codificacao de Hamming.

    Notes
    -----
    So codifica mensagens com 4 bits.

    Examples
    --------
    >>> m = np.array([0,1,0,1])
    >>> codificacao_hamming(m)
    array([0,1,0,1,0,0,1])

        >>> m = np.array([0,1,0,1,0,1,1,1])
    >>> codificacao_hamming(m)
    array([0,1,0,1,0,0,1,0,1,1,1,1,0,0])
    """
    clone_m_stream = copy.copy(m_stream)
    # separa o stream nas varias mensagens
    m_split = np.reshape(clone_m_stream, (-1, 4))
    # aplica o codigo e hamming a cada mensagem
    c_split = (np.dot(m_split, G) % 2).astype(int)
    # junta as mensagens todas num array 1D
    c_stream = c_split.flatten()
    return c_stream

def descodificacao_hamming(c_stream):
    """Descodifica um array binario de N palavras utilizando a 
        descodificacao de hammming, deteta e corrige os erros nas mensagens.

    Parameters
    ----------
    c_stream : ndarray 1D de N palavras onde serão aplicadas a 
        descodificacao de hamming.

    Returns 
    -------
    m_stream : ndarray 1D da mensagem original.

    Notes
    -----
    So descodifica palavras com 7 bits.

    Examples
    --------
    >>> m = np.array([0,1,0,1,0,0,1])
    >>> descodificacao_hamming(m)
    array([0,1,0,1])

        >>> m = np.array([0,1,0,1,0,0,1,0,1,1,1,1,0,0])
    >>> descodificacao_hamming(m)
    array([0,1,0,1,0,1,1,1])
    """
    copy_c_stream = copy.copy(c_stream)
    # separa o stream nas varias palavras
    c_split = np.reshape(copy_c_stream, (-1, 7))
    # calcula o sindroma para cada mensagem
    s_split = np.dot(c_split, H) % 2
    # loop que percorre todas a palavras, detecta e corrige os erros
    for i in range(len(s_split)):
        # calcula o indice de cada erro
        err_idx = np.where(np.all(H == s_split[i], axis=1))[0]
        # verifica se indice de erro para cada mensagem
        if(err_idx.size != 0):
            # corrige o erro
            c_split[i, err_idx[0]] = not bool(c_split[i, err_idx[0]])
    # retira os bits de detecao de erros
    m_split = np.delete(c_split, [4,5,6], axis=1)
    # junta as mensagens todas num array 1D
    m_stream = m_split.flatten()
    return m_stream

def main():
    #exercicio 3

    # definicao de um seed para os as mensagens enviadas sejam sempre as mesmas
    np.random.seed(10)
    # criacao de uma stream de aleatorios formanbdo N / 4 mensagens
    mx = np.random.choice(2,4000)
    # codificacao usando o codigo de hamming
    cx = codificacao_hamming(mx)
    # ndarray com os valores de BER
    BER = np.arange(.1, 1., 0.1)
    #loop para realizar a descodificaçcao com cada BER diferente
    for i in range(len(BER)):
        # reset do random seed
        np.random.seed(None)
        # simulacao do canal
        cy = 1 * np.logical_xor(cx, np.random.binomial(1, BER[i], len(cx)))
        my = descodificacao_hamming(cy)
        # numero de bits das mensagens
        nbits_msg  = mx.size
        # numero de bits das palavras
        nbits_plv = cx.size
        # numero de bits errados das palavras depois de passarem o canal
        err_plv = cx[cy!=cx].size
        # numero de bits errados das mensagens com o detector de erros
        err_msg = my[my!=mx].size

        print("============================================")
        print("BER:      ", round(BER[i], 2))
        print("nbits_msg:", nbits_msg)
        print("nbits_plv:", nbits_plv)
        print("err_plv:  ", err_plv)
        print("err_msg:  ", err_msg)
        print("BER sem correcao:", float(err_plv) / nbits_plv)
        print("BER com correcao:", float(err_msg) / nbits_msg)
