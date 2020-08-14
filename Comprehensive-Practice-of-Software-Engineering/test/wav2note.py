import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def loadFile(filename,rate):
    if filename[-3:-1] != 'wav' or type(rate)!=int:
        return False
    path='music\\'
    path=path+filename
    y,sr=librosa.load(path,sr=rate)
    return y,sr

def music2note(data,rate):
    if type(data)!=np.ndarray or type(rate)!=int or rate==0:
        return False
    
    data=np.transpose(data)
    data=data/data.max()
    data[data<0.75]=0
    unit_rate=rate/(data.shape[1]-1)
    
    Note=[]
    for i in data:
        note=[]
        for j in range(len(i)):
            if i[j]>0 and len(note)==0:
                note.append(librosa.hz_to_note((j+1)*unit_rate))
        if len(note)!=0:
            Note.append(note[0])
    return  Note


def getNoteAndNum(data):
    if type(data) != list:
        return False
    
    data.append('#')
    N=data[0]
    count=1
    Count=[]
    Note=[]
    for i in range(1,len(data)):
        if N==data[i]:
            count=count+1
        if N!=data[i]:
            Count.append(count)
            Note.append(data[i-1])
            count=1
            N=data[i]
    return Note,Count

def Normlize(data,num):
    if type(data) != list or type(num)!=list:
        return False
    Data=[]
    Num=[]
    for i in range(len(data)):
        num[i]=num[i]//10
        if num[i]>=1:
            Data.append(data[i])
            Num.append(num[i])
    return Data,Num


if __name__=='__main__':
    
    y,rate=loadFile('1.wav',44100)
    Time=librosa.get_duration(y,sr=rate)
    fft=librosa.stft(y,n_fft=1024*2)
    D=librosa.amplitude_to_db(abs(fft),ref=np.max)
    D=D+80
    data=music2note(D,rate/2)
    
    data,num=getNoteAndNum(data)
    data,num=Normlize(data,num)

