import json
fileName = 'config.json'
import os
print(os.getcwd())
 
class Options :
    def __init__ (self )  :
        cate1 = json.loads(open(fileName, 'rb').read().decode('utf-8'))  #  'config.json'  파일을 읽어서 딕셔너리로 저장
        self.weight_path  = cate1["weight_path"]
        self.test = cate1["test"]