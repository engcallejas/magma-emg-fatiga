import recursos as r 
import numpy as np

def recorido():
    bufer=[]
    data=r.LR_file(np.random.randint(10),"BaseDatos_EMG_Acc-20230304T150927Z-001\BaseDatos_EMG_Acc")
    n=len(data)/11000
    n2=1/n
    n3=n2*len(data)
    print(f"tamaño {len(data)} delis {len(data)-11000}  Inetero {int(n)} Normal {n} Esto -> {n2} no sé -> {int(n3)}" )
    for i in range(len(data)-11000):
        bufer=[data[i:len(data)+11000]]
        if i == len(data)-11000:
            i=0
    
    bufer=[data[i:len(data)+11000]]
    print(f"{i+11000} tamaño -> {len(data)}")   
    
if __name__=="__main__":
    recorido()