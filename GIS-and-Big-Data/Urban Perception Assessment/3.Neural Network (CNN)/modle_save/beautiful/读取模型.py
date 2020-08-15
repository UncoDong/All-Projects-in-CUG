from tensorflow.keras.models import model_from_json
def GetModle(filname):
    json_file = open(filname+'_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights(filname+'_model.json.h5')
    model.compile(optimizer='rmsprop',loss='mse',metrics=['mae'])
    print('模型加载成功')
    
    # 接下来就可以进行打分了
    # prediction = model.predict(test_data)
    
if __name__ == '__main__':
      GetModle('beautiful')
