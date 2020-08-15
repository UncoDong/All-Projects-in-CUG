# 导入keras
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D,BatchNormalization
import tensorflow as tf


# 导入辅助库
import numpy as np
import matplotlib.pyplot as plt
import pickle
import random



def NeuralNetWork(filname):
    # 输出keras版本
    print(keras.__version__)
    # 得到训练数据
    with open(filname+'_train_data.pickle','rb') as f:
          raw_data,raw_labels=pickle.load(f)
    # 打乱数据
    index = [i for i in range(len(raw_data))]
    random.shuffle(index)
    raw_data = raw_data[index]
    raw_labels = raw_labels[index]
    
    
    midnum = 4500
    raw_data = raw_data[:midnum]
    raw_labels = raw_labels[:midnum]
    raw_data = raw_data.astype('float32')
    print(raw_data.dtype)
    print(raw_data.shape)
    print(raw_labels.shape)
    

    # 将图像的值都压缩在0~1之间
    raw_data = raw_data/255
    raw_labels = raw_labels

    # 前80%作为训练数据
    train_data = raw_data[:int(4*len(raw_data)/5)]
    train_labels = raw_labels[:int(4*len(raw_data)/5)]
    test_data = raw_data[int(4*len(raw_data)/5):]
    test_labels = raw_labels[int(4*len(raw_data)/5):]
    print("得到训练数据完毕")

    # 定义模型
    model = keras.Sequential()

    # 一层卷积层，包含了32个卷积核，大小为3*3
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(300, 480, 3)))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    # 归一化层
    model.add(BatchNormalization())
    # 一个最大池化层，池化大小为2*2
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # 来一个遗忘层
    model.add(Dropout(0.5))
    # 归一化层
    model.add(BatchNormalization())

    # 添加一个卷积层，包含64个卷积和，每个卷积和仍为3*3
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    # 归一化层
    model.add(BatchNormalization())
    # 来一个池化层
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # 来一个遗忘层
    model.add(Dropout(0.5))
    # 归一化层
    model.add(BatchNormalization())

    # 添加一个卷积层，包含64个卷积和，每个卷积和仍为3*3
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    # 归一化层
    model.add(BatchNormalization())
    # 来一个池化层
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # 来一个遗忘层
    model.add(Dropout(0.5))
    # 归一化层
    model.add(BatchNormalization())

              
    # 压平层
    model.add(Flatten())
    # 来一个全连接层
    #model.add(Dense(256, activation='relu'))
    # 最终输出
    model.add(Dense(1))
    # 打印网络结构
    print(model.summary())

    model.compile(optimizer='rmsprop',
                  loss='mse',
                  metrics=['mae'])
    # 分块训练大量数据的块大小
    batch = 64
    # 清空之前model占用的内存，防止OOM
    #tf.reset_default_graph()
    # 重复训练
    history1 = model.fit(train_data, epochs=200,train_labels,batch_size=batch,validation_data = (test_data,test_labels))
    print(history1.history['mae'],history1.history['loss'])
    test_loss, test_acc = model.evaluate(test_data, test_labels)#,batch_size=batch)
    print(test_loss, test_acc)
  

    #根目录
    rootpath = "save_modle/"+filname+"/"
    # 预测的准确性
    print('Test mean_absolute_error:', test_acc)
    # 保存最终的测试结果
    with open(rootpath+filname+"_test.pickle", "wb") as f:
        pickle.dump([test_loss, test_acc ],f)
    
    # 保存模型
    # model.save('my_model.h5')  # creates a HDF5 file 'my_model.h5
    # serialize model to JSON
    model_json = model.to_json()
    with open(rootpath+filname+"_model.json", "w") as json_file:
        json_file.write(model_json)
    #保存模型权重值
    model.save_weights(rootpath+filname+'_model.json.h5')

    # 保存损失
    accy=history1.history['mae']
    lossy = history1.history['loss']
    np_accy = np.array(accy).reshape((1,len(accy))) #reshape是为了能够跟别的信息组成矩阵一起存储
    np_lossy =np.array(lossy).reshape((1,len(lossy)))
    np_out = np.concatenate([np_accy,np_lossy],axis=0)
    np.savetxt(rootpath+filname+'_save.txt',np_out)  
    
    # 保存这个modle
    model.save(rootpath+filname+'_model_all.h5')
    '''
    from tensorflow.keras.models import load_model
    model2 = load_model(rootpath+filname+'_model_all.h5')
    mid = model.predict(test_data)
    print(mid[:100])
    
    from tensorflow.keras.models import model_from_json
    json_file = open(rootpath+filname+'_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights(rootpath+filname+'_model.json.h5')
    model.compile(optimizer='rmsprop',loss='mse',metrics=['mae'])
    mid = model.predict(test_data)
    print(mid[:100])
    '''
    print("保存文件成功")

       


if __name__ == '__main__':
    NeuralNetWork("lively")
        



