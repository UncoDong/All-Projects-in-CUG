import pickle
with open('beautiful_train_data.pickle','rb') as f:
      raw_data,raw_labels=pickle.load(f)
print(raw_data.shape)
print(raw_labels.shape)



