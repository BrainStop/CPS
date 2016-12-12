# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:23:35 2016
@author: David
"""
import sys
sys.path.append("../")
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import trabalhoPratico02.trabalho_pratico02 as tp02

#oejfzieohfjzahglkjrhglkzjerglkjzehg

#ex 1)
#==============================================================================
def codificacao8bit(nbits, signalin):
    """Codificaçao para binario return np.bool binario base 2"""
    #Altera a forma do array sinalIn para  1xLenght(singalIn)
    singal_shape = np.reshape(signalin.astype(np.uint8), (-1, 1))
    #Converte cada linha do array para o seu array binario
    arry_bin = np.unpackbits(singal_shape, axis=1)
    #Splice dos bits necessarios
    arr_bin_spliced = arry_bin[:, np.arange(-nbits, 0)]#
    #Altera o forma do array para unidimensional e retorna-o a np.bool
    return arr_bin_spliced.flatten().astype(np.bool)
   
def codificacao(nbits, signalin):
    if(nbits <= 8):
        return codificacao8bit(nbits, signalin)
#TODO Implementar codificaçcao com nBits superior a 8
#    def codificacao(R,signalIn):
#    arrBin=np.zeros(len(signalIn)*R*1,dtype=np.int64)
#    for i in range(len(signalIn)):
#        val=np.binary_repr(signalIn[i])
#        arrBin[i]=val
#    return arrBin
##output desejado!=[1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,1,1]
#    
def descodificacao(nbits, signalin):
    """descodificacao passa de binario para um np.int64 base 10"""
    #converte o array 1D para XxR
    arr_bin = np.reshape(signalin, (-1, nbits))
    #Descodifica cada linha de valores biarios
    arr_val = np.packbits(arr_bin, axis=-1) >> 8 - nbits
    #Altera o forma do array para unidimensional e retorna-o a np.int64
    return arr_val.flatten().astype(np.int64)
#==============================================================================

def DPCM(nbits, signalin):
    sub_signal = np.roll(signalin, 1)
    sub_signal[0] = 0
    dif_signal = signalin - sub_signal
    val_mid_rise, int_mid_rise = tp02.TabelasMidRise(nbits, np.max(dif_signal))
    y_quant, index_quant = tp02.Quantificador(dif_signal, val_mid_rise, int_mid_rise)
    print(index_quant)
    return codificacao(nbits, index_quant)
    
def _ex2PCM(ficheiro):
    rate, data = wav.read(ficheiro, 'r')
    R = [3, 5, 8]
    SNRarray = []
    for i in range(len(R)):
        val_mid_rise, int_mid_rise = tp02.TabelasMidRise(R[i], np.max(data))
        print(val_mid_rise, int_mid_rise)
        y_quant, index_quant = tp02.Quantificador(val_mid_rise, int_mid_rise, data)
        print("index_quant")
        print(index_quant)
        guitarraCodi = codificacao(R[i], index_quant).astype(int)
        print("guitarracodi")
        print(guitarraCodi.astype(int))
        guitarraDescodi = descodificacao(R[i], guitarraCodi)
        print("descodificacao")
        print(guitarraDescodi.astype(int))
        snrt, snrp = tp02.SNR(guitarraDescodi, R[i], np.max(guitarraDescodi))
        print("snrt")
        print(snrt)
        print("snrp")
        print(snrp)
        SNRarray.append([R[i], snrt, snrp])
        wav.write("guitarraDescodificado"+str(R[i])+"bits.wav", rate, \
                guitarraDescodi.astype('int16'))
    return SNRarray

def main():
    
    """Funcao para resolver os exercicios do enunciado tp03"""
    #3)
    #==========================================================================
    fs = 8000.
    n = np.arange(0, 5)
    freq = 2000.
    pi2 = np.pi * 2

    y = np.cos(pi2 * freq / fs * n)
    R = 3
    nbits = R
    #
    #ex a)
    #usando o quantificador midrise codificaçao!
    #..........................................................................
    a_val_mid_rise, a_int_mid_rise = tp02.TabelasMidRise(R, np.max(y))
    a_y_quant, a_index_quant = tp02.Quantificador(a_val_mid_rise, a_int_mid_rise, y)
    ay_coded = codificacao(nbits, a_index_quant)
    #ex b)
    #..........................................................................
    #usando quantificador Midtread com R=3
    b_val_mid_tread, b_int_mid_tread, b_delta = tp02.tabelasmidtread(R, np.max(y))
    byQuanti, b_index_quant = tp02.Quantificador(b_val_mid_tread, b_int_mid_tread, y)
    by_coded = codificacao(R, b_index_quant)
    #ex c)
    #..........................................................................
    #codificacao DPCM
    cy_coded = DPCM(R, y)
    #==========================================================================

def testToThisFile(files):
    print(_ex2PCM(files))
    
#testToThisFile("../wavFiles/guitarra.wav")
