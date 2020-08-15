import pandas as pd    #导入pandas包

frames = []

def Pandas(emotion,name):
      data = pd.read_csv(emotion+"_"+name+"_data.csv")
      mid = data[emotion]
      mid = mid.values.tolist()
      frames.append(mid)
      
save = []

def GetFinalCsv(csv_name):
      emotions = ['boring','depressing','lively','safety','wealthy']
      for emotion in emotions:
            Pandas(emotion,csv_name)
            
      filname = 'beautiful_'+csv_name+'_data.csv'
      with open(filname,"r") as f:
            for line in f.readlines():
                  # print(line)
                  line = line.split(',')
                  line[len(line)-1] = line[len(line)-1][:-1]
                  save.append(line)
      for k in range(len(emotions)):
            save[0].append(emotions[k])
            for i in range(len(save) - 1):
                  try:
                        save[i+1].append(str(frames[k][i]))
                  except:
                        print(frames[k])
                  
      with open(csv_name+"_data.csv","w") as f:
            for i in range(len(save)):
                  mid = ""
                  for each in save[i]:
                        if each != '':
                              mid+=each
                              mid+=','
                  f.write(mid)
                  f.write('\n')

if __name__ == '__main__':
      GetFinalCsv('Tran_20191229')
      
      
      
      
            
