from music21 import *
import os
import shutil
PitchClass = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
TypeClass = ['64th', '32nd', '16th', 'eighth', 'quarter', 'half', 'whole']
import librosa
import time
import traceback

class StrNote:
    ''''''
    '''
     对音符的字符串信息进行保存
     分别存储pitch，octave ,accidental，并最终拼接起来
    '''

    def __init__(self):
        '''
            默认简谱中的do是C5
            因此是pitch下标为0
            中音的八度octave是第五个
            没有升降号accidsho'wental
            默认是四分之一音符4
            默认没有附点
        '''
        self.pitch = 0
        self.octave = 5
        self.accidental = ''
        self.type = 4
        self.dot = 0

    def __init__(self, pitch):
        '''
          有参构造
        '''
        self.pitch = pitch - 1
        self.octave = 5
        self.accidental = ''
        self.type = 4
        self.dot = 0

    def __add__(self, y):
        '音调pitch加一位'
        self.pitch = (self.pitch + y) % 7
        return self

    def __sub__(self, y):
        '音调pitch减一位'
        self.pitch = (self.pitch + 7 - y) % 7
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
'''
Summay:
    辅助musicstr_to_stream进行处理
    处理是数字的
'''
def deal_is_num(lowerflag,higherflag,shotterflag,sharpflag,each):
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
            # print(midnote)
            sharpflag = False
    return midnote,sharpflag

'''
Summay:
    辅助musicstr_to_stream进行处理
    处理不是数字的
'''
def deal_is_not_num(lowerflag,higherflag,shotterflag,sharpflag,each):
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
    elif each == '>':
        shotterflag -= 1
    return lowerflag,higherflag,shotterflag,sharpflag


'''
Summay:
    添加midstream
'''
def add_mid_stream(notelist,measurenum):
    midstream = stream.Measure(number=measurenum)
    measurenum += 1
    for eachnote in notelist:
        midstream.append(eachnote.getnote())
    return midstream


'''
Summay:
    添加midstream
'''


'''
Summay:
    将字符串简谱转换成音乐流
Parameters:
    music_str - 简谱字符串  str
    play_it - 是否播放      bool
Return：
    s - Music21格式的音乐流 stream
'''
def musicstr_to_stream(music_str, play_it=True):

    s = stream.Score(id='mainScore')
    '''
    lowerflag  -  低音标志()
    higherflag -  高音标志[]
    shotterflag - 短时标志<>
    longgerflag - 长时标志--
    '''
    notelist = []
    lowerflag = False
    higherflag = False
    sharpflag = False
    shotterflag = 0
    measurenum = 1
    print("接受输入",music_str)
    for each in music_str:
        print("每一个",each)
        # print(each)
        if isnum(each):
            midnote,sharpflag = deal_is_num(lowerflag,higherflag,shotterflag,sharpflag,each)
            notelist.append(midnote)
        else:
            lowerflag,higherflag,shotterflag,sharpflag = deal_is_not_num(lowerflag,higherflag,shotterflag,sharpflag,each)
            if each == '.':
                notelist[len(notelist) - 1].adddot()
            elif each == '-':
                notelist[len(notelist) - 1].longer()
            elif each == '#':
                notelist[len(notelist) - 1].setsharp()
            elif each == 'b':
                notelist[len(notelist) - 1].setflat()
            elif each == '|':
                midstream = add_mid_stream(notelist,measurenum)
                s.append(midstream)
                notelist.clear()
            else:
                continue

    if len(notelist) != 0:
        midstream = add_mid_stream(notelist,measurenum)
        s.append(midstream)
    return s


def analyse_each_strnote(each_strnote,type,dot):
    print('正在识别',each_strnote)
    # 如果是<<>>的
    while '<' in each_strnote:
        each_strnote = each_strnote[1:-1]
        type -= 1
        # 如果是长音的
    while '-' in each_strnote:
        each_strnote = each_strnote[1:-1]
        if type == 5 and dot == 0:
            dot = 1
        else:
            type += 1
    return each_strnote,type,dot


'''
Summay:
    将更标准的字符串简谱转换成音乐流
Parameters:
    music_str - 简谱字符串  str
    play_it - 是否播放      bool
Return：
    s - Music21格式的音乐流 stream
'''
def musicstr_char_to_stream(music_str, play_it=True):
    s = stream.Score(id='mainScore')
    str_streams = music_str.split('|')
    measurenum = 0
    for each_stream in str_streams:
        measurenum += 1
        str_notes = each_stream.split(' ')
        # 复点数量
        dot = 0
        # 音长类型
        type = 4
        # 定义每个小节的因父流
        midstream = stream.Measure(number=measurenum)
        for each_strnote in str_notes :
            try:
                if each_strnote == '':
                    continue
                each_strnote,type,dot = analyse_each_strnote(each_strnote,type,dot)
                print('音符识别结果',each_strnote,type,dot)
                thisnote = note.Note(each_strnote)
                thisnote.duration.type = TypeClass[type]
                thisnote.duration.dots = dot
                midstream.append(thisnote)
            except:
                print('出错啦')
                print('当前:',each_strnote)
                print(traceback.format_exc())
        s.append(midstream)
    return s


'''
Summary:   
    根据输入流写入xml，并生成png
return:
    文件名
'''
def write_xml_and_get_png(s):
    #print('此处的文件名',filname)
    png_filname = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    print('写入文件')
    #s.show('text')
    show = s.write('musicxml','./Myapp_covert2musicscore/musicxml/%s.xml'%png_filname)
    print('结果',show)
    #command = '/usr/bin/musescore ./Myapp_covert2musicscore/musicxml/{0}.xml -o ./Myapp_covert2musicscore/static/musicpng/{0}.png'.format(png_filname)
    command = 'MuseScore3 ./Myapp_covert2musicscore/musicxml/{0}.xml -o ./Myapp_covert2musicscore/static/musicpng/{0}.png'.format(png_filname)
    print(command)
    os.system(command)
    return png_filname

'''
Summary:   
    根据输入流写入midi，并生成wav
return:
    文件名
'''
def write_midi_and_get_wav(s):
    wav_filname = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    # 写入midi
    s.write('midi','./Myapp_covert2musicscore/musicfile/%s.mid'%wav_filname)
    # 执行java指令
    os.system('java -jar ./midi2wav.jar ./Myapp_covert2musicscore/musicfile/%s.mid'%wav_filname)
    # 移动文件
    shutil.copyfile('./Myapp_covert2musicscore/musicfile/%s.wav'%wav_filname,'./Myapp_dealfile/static/wavfiles/%s.wav'%wav_filname)
    # 删除原来wav文件
    os.remove('./Myapp_covert2musicscore/musicfile/%s.wav'%wav_filname)

    return wav_filname


if __name__ == '__main__':
    s = musicstr_to_stream("1231|212|312|3123|3123")
    #s.show()
    s.write('musicxml','../musicxml/test.xml')
