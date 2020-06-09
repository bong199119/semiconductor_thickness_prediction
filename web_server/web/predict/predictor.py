# -*- coding: utf-8 -*-

import torch
import modeling
import load_data
import datetime
import os
import pandas as pd

from sqlalchemy import create_engine
import pymysql
# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
# import option


def now_time():
    now = datetime.datetime.now()
    return now

"""# 경로, 디바이스 설정"""
def predict(request,input_tablename,output_tablename):

    # opt = option.Options()
    # weight_path = opt.weight_path
    weight_path = 'C:/Users/bong/project/semiconductor_project/semiconductor_project/web_server/web/predict/test_model_new.pth'

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    """# 데이터 로드"""
    data_realtime = load_data.read_data(input_tablename,output_tablename)

    """# 모델생성"""
    model = modeling.make_model(device, weight_path)

    """# 두께 예측"""
    data_realtime = data_realtime.iloc[:,1:-1]
    data_realtime_numpy = torch.from_numpy(data_realtime.astype(float).values)
    data_realtime_numpy_de = data_realtime_numpy.to(device)
    outputs = model(data_realtime_numpy_de.float()).cpu().detach().numpy()
    # outputs = model(data_realtime_numpy_de.float()).cpu().detach().numpy().round(-1)
    pred_test = pd.DataFrame(outputs)
    pred_test.columns = ['layer_1', 'layer_2', 'layer_3', 'layer_4']

    return pred_test,request



def make_DataFrame(request, pred_test, now, layer):

    # 날자 붙이기
    data_date = pd.DataFrame()
    data_date_temp = pd.DataFrame()
    data_date_temp = data_date_temp.append({'date_now': ''}, ignore_index=True)
    data_date_temp.iat[0, 0] = (now + datetime.timedelta(seconds=0)).strftime('%Y-%m-%d %H:%M:%S')
    data_date = data_date.append(data_date_temp, ignore_index=True)
    data_test = pd.merge(pred_test, data_date, right_index=True, left_index=True)

    # 불량품여부 붙이기
    if (pred_test.iat[0,0] > layer[0]+4) or (pred_test.iat[0,1] > layer[1]+4.5) or (pred_test.iat[0,2] > layer[2]+2.7) or (pred_test.iat[0,3] > layer[3]+2):
        data_infe_temp = pd.DataFrame()
        data_infe_temp = data_infe_temp.append({'inferior': ''}, ignore_index=True)
        data_infe_temp.iat[0, 0] = 'bad'
        data_test = pd.merge(data_test, data_infe_temp, right_index=True, left_index=True)

    else:
        data_infe_temp = pd.DataFrame()
        data_infe_temp = data_infe_temp.append({'inferior': ''}, ignore_index=True)
        data_infe_temp.iat[0, 0] = 'good'
        data_test = pd.merge(data_test, data_infe_temp, right_index=True, left_index=True)

    return data_test, request


def to_DB(request, data_test, output_tablename):

    # engine = create_engine("mysql+mysqldb://root:" + "root1234" + "@localhost/output_data_1", encoding='utf-8')
    engine = create_engine("mysql+mysqldb://root:" + "root1234" + "@localhost/output_data_1", encoding='utf-8')
    conn = engine.connect()

    data_test.to_sql(name=output_tablename, con=engine, if_exists='append',index = False)
    return request


def DB_to_csv(request, output_tablename):

    engine = create_engine("mysql+mysqldb://root:" + "root1234" + "@localhost/output_data_1", encoding='utf-8')
    conn = engine.connect()
    # sql문작성 + 데이터 가져오기
    # sql = 'SELECT * FROM layer_10_160_40_180_output;'
    sql = 'SELECT * FROM '+ output_tablename +';'
    data_read = pd.read_sql(sql, conn)
    # data_read = data_read.drop(data_read.columns[0], axis=1)

    data_read = data_read[['date_now', 'layer_1', 'layer_2', 'layer_3', 'layer_4','inferior']]

    data_read.to_csv("C:/Users/bong/project/semiconductor_project/semiconductor_project/web_server/web/predict/"+output_tablename+"_tomain"+".csv", index=False)
    data_read.iloc[:,:5].to_csv("C:/Users/bong/project/semiconductor_project/semiconductor_project/web_server/web/predict/"+output_tablename+".csv", index=False)
    # print (  "------" )
    # print(data_read)

    return request, data_read


def DB_to_json(request, tablename):

    engine = create_engine("mysql+mysqldb://root:" + "root1234" + "@localhost/output_data_1", encoding='utf-8')
    conn = engine.connect()
    # sql문작성 + 데이터 가져오기
    # sql = 'SELECT * FROM layer_10_160_40_180_output;'
    sql = 'SELECT * FROM '+ tablename +';'
    data_read = pd.read_sql(sql, conn)
    # data_read = data_read.drop(data_read.columns[0], axis=1)

    date_now_tolist = data_read.date_now.tolist()
    layer_1_tolist = data_read.layer_1.tolist()
    layer_2_tolist = data_read.layer_2.tolist()
    layer_3_tolist = data_read.layer_3.tolist()
    layer_4_tolist = data_read.layer_4.tolist()

    dict_data = {
        'columns': [
            date_now_tolist,
            layer_1_tolist,
            layer_2_tolist,
            layer_3_tolist,
            layer_4_tolist
        ]
    }

    return request, dict_data


def to_graph(request):
    # now = now_time()
    # pred_test, request = predict(request)
    # data_test, request = make_DataFrame(request, pred_test, now)
    # to_csv(request, data_test)
    # to_DB(request, data_test)
    tablename = 'layer_10_160_40_180_output'
    request, dict_data = DB_to_json(request, tablename)
    return dict_data

def two_to_graph(request):
    # now = now_time()
    # pred_test, request = predict(request)
    # data_test, request = make_DataFrame(request, pred_test, now)
    # to_csv(request, data_test)
    # to_DB(request, data_test)
    tablename = 'layer_160_200_140_300_output'
    request, dict_data = DB_to_json(request, tablename)
    return dict_data

def to_graph_csv(request):
    layer = [10, 160, 40, 180]
    now = now_time()
    pred_test, request = predict(request,'layer_10_160_40_180_input','layer_10_160_40_180_output')
    data_test, request = make_DataFrame(request, pred_test, now, layer)
    # to_csv(request, data_test)
    to_DB(request, data_test,'layer_10_160_40_180_output')
    request, data_read= DB_to_csv(request,'layer_10_160_40_180_output')
    # # response = load_csv(request)
    response= ""
    return response


def two_to_graph_csv(request):
    layer = [160,200,140,300]
    now = now_time()
    pred_test, request = predict(request,'layer_160_200_140_300_input','layer_160_200_140_300_output')
    data_test, request = make_DataFrame(request, pred_test, now, layer)
    # to_csv(request, data_test)
    to_DB(request, data_test,'layer_160_200_140_300_output')
    request, data_read= DB_to_csv(request,'layer_160_200_140_300_output')
    # # response = load_csv(request)
    response= ""
    return response

# 상세페이지 1공정
def detail_graph_one(request, tablename):

    engine = create_engine("mysql+mysqldb://root:" + "root1234" + "@localhost/output_data_1", encoding='utf-8')
    conn = engine.connect()
    sql_bad = 'SELECT * FROM ' + tablename + ' WHERE inferior = '+'\'bad\''+';'
    data_read_bad = pd.read_sql(sql_bad, conn)
    sql_total = 'SELECT * FROM ' + tablename +';'
    data_read_total = pd.read_sql(sql_total, conn)
    len_bad = (len(data_read_bad)/len(data_read_total))*100
    len_good = ((len(data_read_total)-len(data_read_bad))/len(data_read_total))*100

    dict_data =  [{
       'name': 'bad',
       'y' : len_bad
   }, {
    'name': 'good',
    'y': len_good
   }]

    return dict_data


def detail_graph_DR_onevsT(request, one_table, other_table, process_name):

    engine = create_engine("mysql+mysqldb://root:" + "root1234" + "@localhost/output_data_1", encoding='utf-8')
    conn = engine.connect()
    sql_bad = 'SELECT * FROM ' + one_table[0] + ' WHERE inferior = '+'\'bad\''+';'
    data_read_bad = pd.read_sql(sql_bad, conn)
    sql_bad_2 = 'SELECT * FROM ' + other_table[0] + ' WHERE inferior = '+'\'bad\''+';'
    data_read_bad_2 = pd.read_sql(sql_bad_2, conn)
    len_bad_1 = (len(data_read_bad)/(len(data_read_bad)+len(data_read_bad_2)))*100
    len_bad_2 = (len(data_read_bad_2)/(len(data_read_bad)+len(data_read_bad_2)))*100

    dict_data =  [{
       'name': '제 '+str(process_name)+' 공정 불량품',
       'y' : len_bad_1
   }, {
    'name': '그 외 공정 불량품',
    'y': len_bad_2
   }]

    return dict_data

def detail_graph_DR_progresses(request):

    engine = create_engine("mysql+mysqldb://root:" + "root1234" + "@localhost/output_data_1", encoding='utf-8')
    conn = engine.connect()

    # 1번공정 bad, good 데이터 받아오기
    sql_bad = 'SELECT * FROM ' + 'layer_10_160_40_180_output' + ' WHERE inferior = ' + '\'bad\'' + ';'
    data_read_bad = pd.read_sql(sql_bad, conn)
    sql_good = 'SELECT * FROM ' + 'layer_10_160_40_180_output' + ' WHERE inferior = ' + '\'good\'' + ';'
    data_read_good = pd.read_sql(sql_good, conn)

    # 2번공정 bad, good 데이터 받아오기
    sql_bad_2 = 'SELECT * FROM ' + 'layer_160_200_140_300_output' + ' WHERE inferior = ' + '\'bad\'' + ';'
    data_read_bad_2 = pd.read_sql(sql_bad_2, conn)
    sql_good_2 = 'SELECT * FROM ' + 'layer_160_200_140_300_output' + ' WHERE inferior = ' + '\'good\'' + ';'
    data_read_good_2 = pd.read_sql(sql_good_2, conn)

    # 전체공정_json으로 넘겨줄 데이터
    data_bad_total = len(data_read_bad)+len(data_read_bad_2)
    data_good_total = len(data_read_good)+len(data_read_good_2)
    data_bad_total_total = data_bad_total + data_good_total
    data_bad_total_rate = round(data_bad_total/data_bad_total_total,2)
    data_good_total_rate = round(data_good_total/data_bad_total_total,2)

    # 제1공정_json으로 넘겨줄 데이터
    data_bad_1 = len(data_read_bad)
    data_good_1 = len(data_read_good)
    data_1_total = data_bad_1 + data_good_1
    data_bad_1_rate = round(data_bad_1/data_1_total,2)
    data_good_1_rate = round(data_good_1/data_1_total,2)


    # 제2공정_json으로 넘겨줄 데이터
    data_bad_2 = len(data_read_bad_2)
    data_good_2 = len(data_read_good_2)
    data_2_total = data_bad_2 + data_good_2
    data_bad_2_rate = round(data_bad_2/data_2_total,2)
    data_good_2_rate = round(data_good_2/data_2_total,2)




    dict_data = [{
    'name': 'bad',
    'data': [data_bad_total_rate, data_bad_1_rate, data_bad_2_rate]
  }, {
    'name': 'good',
    'data': [data_good_total_rate, data_good_1_rate, data_good_2_rate]
  }]

    return dict_data


def goto_get_quantity(request, tablename):

    engine = create_engine("mysql+mysqldb://root:" + "root1234" + "@localhost/output_data_1", encoding='utf-8')
    conn = engine.connect()
    sql_total = 'SELECT * FROM ' + tablename + ';'
    data_read_total = pd.read_sql(sql_total, conn)
    sql_good = 'SELECT * FROM ' + tablename + ' WHERE inferior = ' + '\'good\'' + ';'
    data_read_good = pd.read_sql(sql_good, conn)
    sql_bad = 'SELECT * FROM ' + tablename + ' WHERE inferior = ' + '\'bad\'' + ';'
    data_read_bad = pd.read_sql(sql_bad, conn)

    dict_data =[
        '전체 데이터 수량 : ' +str(len(data_read_total)),'\n'
    
        '정상 수량 : ' + str(len(data_read_good)),'\n'
    
        '불량 수량 : ' + str(len(data_read_bad))
   ]

    return dict_data

def goto_reflec(request, input_tablename, output_tablename):

    engine = create_engine("mysql+mysqldb://root:" + "root1234" + "@localhost/output_data_1", encoding='utf-8')
    conn = engine.connect()
    sql_total = 'SELECT * FROM ' + output_tablename + ';'
    output_now = pd.read_sql(sql_total, conn)
    number = len(output_now)
    engine = create_engine("mysql+mysqldb://root:" + "root1234" + "@localhost/test_data", encoding='utf-8')
    conn = engine.connect()
    sql_total = 'SELECT * FROM ' + input_tablename +' WHERE NUMBER < '+ str(number)+ ';'
    data_read_total = pd.read_sql(sql_total, conn)
    data_read_total.iloc[:,3:].to_csv(str(input_tablename)+'_X.csv', index=False)

    return request

