# -*- coding: utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

def read_data(input_tablename, output_tablename):
  # db에 붙이기  test_data -> 데이터베이스명, root1234 -> DB비밀번호
  len_data_read = read_data_len(output_tablename)
  engine = create_engine("mysql+mysqldb://root:"+"root1234"+"@localhost/test_data", encoding='utf-8')
  conn = engine.connect()

  # sql문작성 + 데이터 가져오기
  # sql = 'SELECT * FROM layer_10_160_40_180_input WHERE number = 0;'
  # sql = 'SELECT * FROM layer_10_160_40_180_input'+';'
  # data_read = pd.read_sql(sql, conn)

  # sql_load = 'SELECT * FROM layer_10_160_40_180_input WHERE number = '+str(len_data_read)+';'
  sql_load = 'SELECT * FROM '+ input_tablename +' WHERE number = ' + str(len_data_read) + ';'
  data_read = pd.read_sql(sql_load, conn)
  data_read = data_read.drop(data_read.columns[0], axis=1)

  return data_read

def read_data_len(output_tablename):
  engine = create_engine("mysql+mysqldb://root:"+"root1234"+"@localhost/output_data_1", encoding='utf-8')
  conn = engine.connect()
  # sql = 'SELECT * FROM layer_10_160_40_180_output;'
  sql = 'SELECT * FROM '+output_tablename+';'
  data_read = pd.read_sql(sql, conn)
  len_data_read = len(data_read)
  return len_data_read
