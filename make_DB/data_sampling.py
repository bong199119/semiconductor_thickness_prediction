# -*- coding: utf-8 -*-

import pandas as pd
import random
import datetime

data = pd.read_csv('../../semiconductor_train.csv')

# 인덱스 무작위로 5개 뽑기
# -> 공정이 5개라고 가정하고 무작위로 5개의 인덱스를 뽑는과정
# -> 인덱스는 train데이터셋의 인덱스
# def sample_index():
#     numbers = []
#     for i in range (5):
#         numbers.append(random.randint(1,810000))
#     print(numbers)
#     return numbers

def init():
    numbers = [460217, 422520, 771294, 13608, 520882]
    now = datetime.datetime.now()

    return numbers, now

"""# 첫번째 테이블 제작"""
def make_table1(numbers, now):
    i = numbers[0]
    data_test1 = data.iloc[i - 1:i, :]
    data_test_temp = data.iloc[i - 1:i, :]

    data_date = pd.DataFrame()
    data_date_temp = pd.DataFrame()
    data_date_temp = data_date_temp.append({'date': ''}, ignore_index=True)

    for i in range(499):
        data_test1 = data_test1.append(data_test_temp, ignore_index=True)

    for i in range(500):
        for j in range(4, 230):
            data_test1.iloc[i, j] = data_test1.iloc[i, j] + random.uniform(-0.01, 0.01)

    for i in range(500):
        data_date_temp.iat[0, 0] = (now + datetime.timedelta(seconds=i * 3)).strftime('%Y-%m-%d %H:%M:%S')
        data_date = data_date.append(data_date_temp, ignore_index=True)

    data_test1 = pd.merge(data_test1, data_date, right_index=True, left_index=True)

    data_test1.to_csv('data_test1.csv')


"""# 두번째 테이블 제작"""
def make_table2(numbers, now):
    i = numbers[1]
    data_test2 = data.iloc[i - 1:i, :]
    data_test_temp2 = data.iloc[i - 1:i, :]

    data_date = pd.DataFrame()
    data_date_temp = pd.DataFrame()
    data_date_temp = data_date_temp.append({'date': ''}, ignore_index=True)

    for i in range(499):
        data_test2 = data_test2.append(data_test_temp2, ignore_index=True)

    for i in range(500):
        for j in range(4, 230):
            data_test2.iloc[i, j] = data_test2.iloc[i, j] + random.uniform(-0.01, 0.01)

    for i in range(500):
        data_date_temp.iat[0, 0] = (now + datetime.timedelta(seconds=i * 3)).strftime('%Y-%m-%d %H:%M:%S')
        data_date = data_date.append(data_date_temp, ignore_index=True)

    data_test2 = pd.merge(data_test2, data_date, right_index=True, left_index=True)

    data_test2.to_csv('data_test2.csv')


"""# 세번째 테이블 제작"""
def make_table3(numbers, now):
    i = numbers[2]
    data_test3 = data.iloc[i - 1:i, :]
    data_test_temp3 = data.iloc[i - 1:i, :]

    data_date = pd.DataFrame()
    data_date_temp = pd.DataFrame()
    data_date_temp = data_date_temp.append({'date': ''}, ignore_index=True)

    for i in range(499):
        data_test3 = data_test3.append(data_test_temp3, ignore_index=True)

    for i in range(500):
        for j in range(4, 230):
            data_test3.iloc[i, j] = data_test3.iloc[i, j] + random.uniform(-0.01, 0.01)

    for i in range(500):
        data_date_temp.iat[0, 0] = (now + datetime.timedelta(seconds=i * 3)).strftime('%Y-%m-%d %H:%M:%S')
        data_date = data_date.append(data_date_temp, ignore_index=True)

    data_test3 = pd.merge(data_test3, data_date, right_index=True, left_index=True)

    data_test3.to_csv('data_test3.csv')


"""# 네번째 테이블 제작"""
def make_table4(numbers, now):
    i = numbers[3]
    data_test4 = data.iloc[i - 1:i, :]
    data_test_temp4 = data.iloc[i - 1:i, :]

    data_date = pd.DataFrame()
    data_date_temp = pd.DataFrame()
    data_date_temp = data_date_temp.append({'date': ''}, ignore_index=True)

    for i in range(499):
        data_test4 = data_test4.append(data_test_temp4, ignore_index=True)

    for i in range(500):
        for j in range(4, 230):
            data_test4.iloc[i, j] = data_test4.iloc[i, j] + random.uniform(-0.01, 0.01)

    for i in range(500):
        data_date_temp.iat[0, 0] = (now + datetime.timedelta(seconds=i * 3)).strftime('%Y-%m-%d %H:%M:%S')
        data_date = data_date.append(data_date_temp, ignore_index=True)

    data_test4 = pd.merge(data_test4, data_date, right_index=True, left_index=True)

    data_test4.to_csv('data_test4.csv')


"""# 다섯번째 테이블"""
def make_table5(numbers, now):
    i = numbers[4]
    data_test5 = data.iloc[i - 1:i, :]
    data_test_temp5 = data.iloc[i - 1:i, :]

    data_date = pd.DataFrame()
    data_date_temp = pd.DataFrame()
    data_date_temp = data_date_temp.append({'date': ''}, ignore_index=True)

    for i in range(499):
        data_test5 = data_test5.append(data_test_temp5, ignore_index=True)

    for i in range(500):
        for j in range(4, 230):
            data_test5.iloc[i, j] = data_test5.iloc[i, j] + random.uniform(-0.01, 0.01)

    for i in range(500):
        data_date_temp.iat[0, 0] = (now + datetime.timedelta(seconds=i * 3)).strftime('%Y-%m-%d %H:%M:%S')
        data_date = data_date.append(data_date_temp, ignore_index=True)

    data_test5 = pd.merge(data_test5, data_date, right_index=True, left_index=True)

    data_test5.to_csv('data_test5.csv')


def make_table():
    numbers, now = init()
    make_table1(numbers, now)
    make_table2(numbers, now)
    make_table3(numbers, now)
    make_table4(numbers, now)
    make_table5(numbers, now)

"""# main 실행"""
if __name__ == "__main__":
    make_table()







