import librosa
import numpy as np
import matplotlib.pyplot as plt

def load_file(filename,rate):
    path=filename
    y,sr=librosa.load(path,sr=rate)
    return y,sr

def music_to_note(data,rate):
    data=np.transpose(data)
    data=data/data.max()
    data[data<0.75]=0

    unit_rate=rate/(data.shape[1]-1)
    note_list=[]

    for i in data:
        note=[]
        for j in range(len(i)):
            if i[j]>0 and len(note)==0:
                note.append(librosa.hz_to_note((j+1)*unit_rate))
        if len(note)!=0:
            note_list.append(note[0])

    return  note_list

def get_note_and_num(data):
    data.append('#')
    N=data[0]
    count=1
    count_list=[]
    note_list=[]
    for i in range(1,len(data)):
        if N==data[i]:
            count=count+1
        if N!=data[i]:
            count_list.append(count)
            note_list.append(data[i-1])
            count=1
            N=data[i]
    return note_list,count_list

def normlize(data,num):
    data_list=[]
    num_list=[]
    for i in range(len(data)):
        num[i]=num[i]//10
        if num[i]>=1:
            data_list.append(data[i])
            num_list.append(num[i])
    return data_list,num_list

def save_file(filename,data,num=None):
    if num!=None:
        output = open(filename,'w+')
        for i in range(len(data)):
            output.write(data[i])
            output.write(' ')
            output.write(str(num[i]))
            output.write('\n')
        output.close()
    elif num==None:
        output = open(filename,'w+')
        for i in range(len(data)):
            output.write(data[i])
            output.write(' ')
            output.write('\n')
        output.close()

def note_to_note(data):
    data_list=[]
    note_dic={'C5':'1','D5':'2','E5':'3','F5':'4','G5':'5','A5':'6','B5':'7',
             'C4':'(1)','D4':'(2)','E4':'(3)','F4':'(4)','G4':'(5)','A4':'(6)','B4':'(7)',
             'C6':'[1]','D6':'[2]','E6':'[3]','F6':'[4]','G6':'[5]','A6':'[6]','B6':'[7]'}
    for x in data:
        if x not in note_dic.keys():
            data_list.append('#')
        else:
            data_list.append(note_dic[x])
    return data_list

def single_note(filename,sr):
    y,rate=librosa.load(filename,sr)
    fft=librosa.stft(y,n_fft=1024*2)
    D=librosa.amplitude_to_db(abs(fft),ref=np.max)
    D=D+80
    data=music_to_note(D,rate/2)
    data_2=note_to_note(data)
    return data,data_2

def merge_note(filename,sr):
    y,rate=load_file(filename,sr)
    fft=librosa.stft(y,n_fft=1024*2)
    D=librosa.amplitude_to_db(abs(fft),ref=np.max)
    D=D+80
    data=music_to_note(D,rate/2)
    data,num=get_note_and_num(data)
    data,num=normlize(data,num)
    data_2=note_to_note(data)
    return data,data_2,num

def plib(data):
    plt.figure()
    librosa.display.specshow(data,sr=44100,x_axis='time',y_axis='log')
    plt.show()

if __name__=='__main__':
    y,rate=librosa.load('./huanlesong.wav',sr=44100)
    fft=librosa.stft(y,n_fft=1024*2)
    D=librosa.amplitude_to_db(abs(fft),ref=np.max)
    D=D+80
    data=music_to_note(D,rate/2)
    data,num=get_note_and_num(data)
    print(data,num)

