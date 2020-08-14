from music21 import *
import librosa
import matplotlib.pyplot as plt
import numpy as np


PitchClass = ['C','D','E','F','G','A','B']
TypeClass = ['64th','32nd','16th','eighth','quarter','half','whole']   
class StrNote:
    '''
     对音符的字符串信息进行保存
     分别存储pitch，octave ,accidental，并最终拼接起来
    '''
    def __init__(self):
        '''
            默认简谱中的do是C5
            因此是pitch下标为0
            中音的八度octave是第五个
            没有升降号accidental 
            默认是四分之一音符4
            默认没有附点
        '''
        self.pitch = 0
        self.octave = 5
        self.accidental = ''
        self.type = 4
        self.dot = 0
        
    def __init__(self,pitch):
        '''
          有参构造
        '''
        self.pitch = pitch-1
        self.octave = 5
        self.accidental = ''
        self.type = 4
        self.dot = 0
            
    def __add__(self, y):
        '音调pitch加一位'
        self.pitch = (self.pitch+y)%7
        return self
        
    def __sub__(self,y):
        '音调pitch减一位'
        self.pitch = (self.pitch+7-y)%7
        return self
    
    def setflat(self):
        '降音'
        self.accidental = 'b'
    
    def setsharp(self):
        '升音'
        self.accidental = '#'
    
    def setnormal(self):
        '变成普通音'
        self.accidental = ''
        
    def higher(self):
        '提高一个八度'
        self.octave += 1 
        
    def lower(self):
        '降低一个八度'
        self.octave -= 1 
    
    def longer(self):
        '时间加长'
        if self.type == 5 and self.dot == 0:
            self.dot = 1
        else:
            self.type += 1
            
    def shotter(self):
        '时间减短'
        self.type -= 1
    
    def adddot(self):
        '添加附点'
        self.dot += 1
        
    def getstr(self):
        '返回这个音的字符串'
        return str(PitchClass[self.pitch]) + str(self.octave) + str(self.accidental)
        
    
    def getnote(self):
        if self.pitch == -1:
            stopnote = note.Rest(1)
            stopnote.duration.type = TypeClass[self.type]
            stopnote.duration.dots = self.dot
            return stopnote
        '返回音符对象'
        thisnote = note.Note(str(PitchClass[self.pitch]) + str(self.octave) + str(self.accidental))
        thisnote.duration.type = TypeClass[self.type]
        thisnote.duration.dots = self.dot
        return thisnote
 
'''判断是数字还是符号'''
def isnum(input):
    try:
        int(input)
        return True
    except:
        return False


def str2tone(music_str):
    #out_put = open('out.txt','w')
    notelist = []
    s = stream.Score(id='mainScore')
    '''
    lowerflag  -  低音标志()
    higherflag -  高音标志[]
    shotterflag - 短时标志<>
    longgerflag - 长时标志--
    
    '''
    lowerflag = False
    higherflag = False
    sharpflag = False
    shotterflag = 0
    measurenum = 1
    left = ''
    right = ''
    for each in music_str:
        #print(each)
        if isnum(each):
            midnote = StrNote(int(each))
            if lowerflag == True:
                midnote.lower()
            if higherflag == True:
                midnote.higher()
            if shotterflag != 0:
                for i in range(shotterflag):
                    midnote.shotter()
            if sharpflag == True:
                midnote.setsharp()
                #print(midnote)
                sharpflag = False
            notelist.append(midnote)
        else:
            if each == '(':
                lowerflag = True
            elif each == ')':
                lowerflag = False
            elif each == '[':
                higherflag = True 
            elif each == ']':
                higherflag = False 
            elif each == '<':
                shotterflag += 1 
                left = '<'+left
            elif each == '>':
                shotterflag -= 1
                right = right+'>'
            elif each == '.':
                notelist[len(notelist)-1].adddot()
                right = right+'.'
            elif each == '-':
                notelist[len(notelist)-1].longer()
                right = right+'-'
            elif each == '#':
                #sharpflag = True
                notelist[len(notelist)-1].setsharp()
            elif each == 'b':
                notelist[len(notelist)-1].setflat()
    
    return left+notelist[0].getstr()+right


tone_list = ['1','2','3','4','5','6','7']


def music2note1(data,unit_rate):
    if data.max() == 0:
        return None
    index = (data!=0).argmax(axis=0)
    return librosa.hz_to_note((index+1)*unit_rate)


def music2note2(i,unit_rate):
    note = []
    for j in range(len(i)):
        #第一个非0值
        if i[j]>0 and len(note)==0:
            #频率转换音符
            note_str = librosa.hz_to_note((j+1)*unit_rate)
            note.append(note_str)
    if len(note)==1:
        return note[0]
    return  None
