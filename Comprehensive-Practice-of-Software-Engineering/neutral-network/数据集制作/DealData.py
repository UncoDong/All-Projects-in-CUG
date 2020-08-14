import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


def music2note(data,rate):
    #转置 降噪
    data=np.transpose(data)
    data=data/data.max()
    data[data<0.75]=0

    #单位频率
    unit_rate=rate/(data.shape[1]-1)
    Note=[]

    for i in data:
        note=[]
        for j in range(len(i)):
            #第一个非0值
            if i[j]>0 and len(note)==0:
                #频率转换音符
                note.append(librosa.hz_to_note((j+1)*unit_rate))
                
        if len(note)!=0:
            Note.append(note[0])
    return  Note

def ChangeMuisc2Note():
    y,rate=librosa.load('2020-05-26_21_11_44_0.wav',44100)
    #短时傅里叶
    fft=librosa.stft(y,n_fft=1024*2)
    #转换为分贝值
    D=librosa.amplitude_to_db(abs(fft),ref=np.max)
    #数据>0
    D=D+80
    
    data=music2note(D,rate/2)

    output=open('note.txt','w+')
    for i in range(len(data)):
        output.write(data[i])
        output.write('\n')
    output.close()
    return data
    
if __name__=='__main__':
    data=ChangeMuisc2Note()


    
