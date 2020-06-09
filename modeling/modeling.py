# -*- coding: utf-8 -*-

import torch
import random
import os.path 
import torch.nn as nn

# gpu 사용여부 확인
use_cuda = torch.cuda.is_available()

# 랜덤 시드 생성
random.seed(777)
torch.manual_seed(777)
if use_cuda:
    torch.cuda.manual_seed_all(777)

# 모델 생성
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


# 모델 생성 함수 (device = 'cuda' or 'cpu'), (weight_path = 가중치 파일 경로)
def make_model(device,weight_path):
  
    file = weight_path

    # 가중치 파일이 있다면 가중치 불러와서 적용
    if os.path.isfile(file):
      
      device = torch.device(device) # 가중치를 제작할 때 device와 사용할때 device를 맞춰주어야 한다.
      model = MLPRegressor() # 모델 생성
      model.load_state_dict(torch.load(file, map_location=device)) # 모델에 가중치 적용
      model.eval() # 드롭아웃 및 배치 정규화에 일관성 부여
      print("Yes. it is a file")

    # 가중치 파일이 없다면 새로운 모델을 만들기
    else : 
      model = MLPRegressor()
      print("create a new model")

    return model

    # make_model()함수가 존재하는 이유는 모델학습에 매우 많은 시간이 들어간다 (epoch가 150번정도일때 2주일정도)
    # 현재모델은 epoch를 1000번으로 설정했기 때문에 모델을 학습하다가 세션이 종료되는 경우도 있고 colab에서의 gpu사용량이 한계치에 달해
    # 런타임이 종료 될 수가 있다. 따라서 세션을 새로 시작해야 하므로 make_model()함수가 필요
