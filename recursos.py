import pandas  as pd
import os
import numpy as np
from scipy.signal import hilbert, savgol_filter

def suavizar(signal, ventana, polyorder):
    signal_smooth = savgol_filter(signal, ventana, polyorder)
    return signal_smooth

def envolvente(signal):
    analytic_signal = hilbert(signal)
    amplitude_envelope = np.abs(analytic_signal)
    return amplitude_envelope


def zerOut(signal):
    c = 0
    for i in range(len(signal)):
        if signal[i] == 0:
            c = c + 1
        else:
            break

    for i in range(c):
        signal.pop(0)
    return signal

def LR_file(i,ruta):
    emg=[]
    archivos=os.listdir(ruta)
    
    data = pd.read_excel(f'{ruta}/{archivos[i]}')
    nombresCol=data.columns
    emg_temp = data[nombresCol[0]]
    
    print(archivos[i])
    
    emg=[i for i in emg_temp]

    emg_final=zerOut(emg)    
        
    return(emg_final)


if __name__=="__main__":
    archivos = LR_file(1,"BaseDatos_EMG_Acc-20230304T150927Z-001/BaseDatos_EMG_Acc")
    