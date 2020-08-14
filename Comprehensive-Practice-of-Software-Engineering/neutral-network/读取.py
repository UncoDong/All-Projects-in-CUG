
'''
Summary:
    读取保存了 wav文件名:音符 对应的字典
Return
    music_dic - 字典
'''

import pickle
def GetMusicDic():
    with open('wavDatasets/music_dic.pkl', 'rb') as file:
        music_dic = pickle.load(file)
    return music_dic


print(GetMusicDic())



for each in GetMusicDic()['2020-05-26_21_11_44_0']:
    print(each)
