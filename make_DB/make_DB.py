# -*- coding: utf-8 -*-

# pip install pymysql
# pip install sqlalchemy
# -> 설치 필요함

# data_sampling 불러오기
from data_sampling  import make_table
from sqlalchemy import create_engine
import pandas as pd
import pymysql
# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

"""# 첫번째 DB"""
def make_first_DB():
    data = pd.read_csv('data_test1.csv')
    data = data.drop(data.columns[1:5],axis = 1)
    data = data.rename({'Unnamed: 0':'number'},axis = 'columns')
    engine = create_engine("mysql+mysqldb://root:"+"root1234"+"@localhost/test_data", encoding='utf-8')
    conn = engine.connect()
    data.to_sql(name='layer_180_20_110_170_input', con=engine, if_exists='append')

"""# 두번째 DB"""
def make_second_DB():
    data = pd.read_csv('data_test2.csv')
    data = data.drop(data.columns[1:5],axis = 1)
    data = data.rename({'Unnamed: 0':'number'},axis = 'columns')
    engine = create_engine("mysql+mysqldb://root:"+"root1234"+"@localhost/test_data", encoding='utf-8')
    conn = engine.connect()
    data.to_sql(name='layer_160_200_140_300_input', con=engine, if_exists='append')

"""# 세번째 DB"""
def make_third_DB():
    data = pd.read_csv('data_test3.csv')
    data = data.drop(data.columns[1:5],axis = 1)
    data = data.rename({'Unnamed: 0':'number'},axis = 'columns')
    engine = create_engine("mysql+mysqldb://root:"+"root1234"+"@localhost/test_data", encoding='utf-8')
    conn = engine.connect()
    data.to_sql(name='layer_290_170_300_240_input', con=engine, if_exists='append')

"""# 네번째 DB"""
def make_fourth_DB():
    data = pd.read_csv('data_test4.csv')
    data = data.drop(data.columns[1:5],axis = 1)
    data = data.rename({'Unnamed: 0':'number'},axis = 'columns')
    engine = create_engine("mysql+mysqldb://root:"+"root1234"+"@localhost/test_data", encoding='utf-8')
    conn = engine.connect()
    data.to_sql(name='layer_10_160_40_180_input', con=engine, if_exists='append')

"""# 다섯번째 DB"""
def make_fifth_DB():
    data = pd.read_csv('data_test5.csv')
    data = data.drop(data.columns[1:5],axis = 1)
    data = data.rename({'Unnamed: 0':'number'},axis = 'columns')
    engine = create_engine("mysql+mysqldb://root:"+"root1234"+"@localhost/test_data", encoding='utf-8')
    conn = engine.connect()
    data.to_sql(name='layer_200_90_230_220_input', con=engine, if_exists='append')


def main():
    #테이블 생성
    make_table()
    make_first_DB()
    make_second_DB()
    make_third_DB()
    make_fourth_DB()
    make_fifth_DB()


if __name__ == "__main__":
    main()

