# -*- coding: utf-8 -*-
import torch
import random
import os.path 
import torch.nn as nn

# cuda사용가능 여부 check
use_cuda = torch.cuda.is_available()

# 랜덤 시드 생성
random.seed(777)
torch.manual_seed(777)
if use_cuda:
    torch.cuda.manual_seed_all(777)

# 모델 구성
class MLPRegressor(nn.Module):
    def __init__(self):
        super(MLPRegressor, self).__init__()
        
        
        self.hidden = nn.Sequential(
            
        nn.Linear(226, 768),
        nn.BatchNorm1d(768),
        nn.Linear(768, 768),
        nn.ReLU(),
        nn.Dropout(0.2),
        nn.Linear(768, 768),
        nn.BatchNorm1d(768),
        nn.ReLU(),
        nn.Dropout(0.2),
        nn.Linear(768, 768),
        nn.BatchNorm1d(768),
        nn.ReLU(),
        nn.Dropout(0.2),
        nn.Linear(768, 384),
        nn.ReLU(),
        nn.Dropout(0.2),
        nn.Linear(384, 4)

        )
        if use_cuda:
            self.hidden = self.hidden.cuda()
    def forward(self, x):
        o = self.hidden(x)
        return o

# 모델제작 함수
def make_model(device, weight_path):
  
    file = weight_path

    # 가중치 파일이 있으면 가져와서 적용
    if os.path.isfile(file):
      
      device = torch.device(device) 
      model = MLPRegressor()
      model.load_state_dict(torch.load(file, map_location=device))
      model.eval()
      print("model created")

    else : 
      model = MLPRegressor()
      print("there is a problem")

    return model
