# -*- coding: utf-8 -*-

import torch.utils.data as data_utils
import torch
import pandas as pd
from sklearn.model_selection import train_test_split

# train 데이터 로드하는 함수. (path는 트레인데이터 경로)
def load_splitter(path):

  data = pd.read_csv(path)

  # 데이터를 X와 label로 나누기
  data_y = data.iloc[:,0:4]
  data_X = data.iloc[:,4:]
    
  batch_size = 100

  # train_test_split
  X_train, X_test ,y_train, y_test = train_test_split(data_X, data_y, test_size =0.2, shuffle = True, random_state = 34)

  trn_X = torch.from_numpy(X_train.astype(float).values)
  trn_y = torch.from_numpy(y_train.astype(float).values)
  val_X = torch.from_numpy(X_test.astype(float).values)
  val_y = torch.from_numpy(y_test.astype(float).values)


  class Dataset(data_utils.Dataset):
    
    def __init__(self, X, y):
        self.X = X
        self.y = y
    
    def __getitem__(self, idx):
        return {'X': self.X[idx], 'y': self.y[idx]}
    
    def __len__(self):
        return len(self.X)


  # batch_size만큼 잘라서 데이터 로드
  trn = Dataset(trn_X, trn_y)
  trn_loader = data_utils.DataLoader(trn, batch_size=batch_size, shuffle=True)

  val = Dataset(val_X, val_y)
  val_loader = data_utils.DataLoader(val, batch_size=batch_size, shuffle=False)


  return trn, val, trn_X, trn_y, val_X, val_y, trn_loader, val_loader
