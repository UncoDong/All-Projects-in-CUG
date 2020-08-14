import json

#SAVE_PATH = '/workspace/MusicBackEnd/Myapp_runweb/static/json/'
SAVE_PATH = './Myapp_runweb/static/json/'
def make_each_dic(score_name,wav_url,png_url,user_name):
    return {"score_name":score_name,"wav_url":wav_url,'png_url':png_url,'user_name':user_name}


def make_user_json(score_list):
    musicscore = []
    for each in score_list:
        print(each)
        musicscore.append(make_each_dic(each.score_name,"/Myapp_dealfile/downloadfile/"+each.wav_path,"/static/musicpng/"+each.png_path,each.user_name))

    # for i in range(2):
    #     musicscore.append(make_each_dic("第一曲谱","www.baidu.com"))

    cbUser = 'cbUser({"musicscore":'+str(musicscore)+'})'
    #dumps 将数据转换成字符串
    #json_str = json.dumps(cbUser,indent=4)# 使用indent格式化输出

    # 保存文件
    with open(SAVE_PATH+"user.json","w",encoding='utf-8') as f:
         f.write(cbUser)
         print("保存json完成")


def make_all_json(score_list):
    musicscore = []
    for each in score_list:
        musicscore.append(make_each_dic(each.score_name,"/Myapp_dealfile/downloadfile/"+each.wav_path,"/static/musicpng/"+each.png_path,each.user_name))

    # for i in range(2):
    #     musicscore.append(make_each_dic("第一曲谱","www.baidu.com"))

    cbUser = 'cbAll({"musicscore":'+str(musicscore)+'})'
    #dumps 将数据转换成字符串
    #json_str = json.dumps(cbUser,indent=4)# 使用indent格式化输出

    # 保存文件
    with open(SAVE_PATH+"all.json","w",encoding='utf-8') as f:
         f.write(cbUser)
         print("保存json完成")
