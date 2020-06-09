from django.shortcuts import render

# Create your views here.
# -*- encoding:utf8 -*-

from django.shortcuts import render, HttpResponse, render

import sys
sys.path.append('C:/Users/bong/project/semiconductor_project/semiconductor_project/web_server/web/predict')
import predictor
import random, json


# Create your views here.

def home_page(request):
    return render(request,'home.html')

def realtime_analysis(request):
    return render(request,'realtime_analysis.html')

def detail_analysis(request):
    return render(request,'detail_analysis.html')

def two_detail_analysis(request):
    return render(request,'two_detail_analysis.html')

def synthesis_detail_analysis(request):
    return render(request,'synthesis_detail_analysis.html')

def main_realtime_analysis(request):
    return render(request,'main_realtime_analysis.html')

def to_graph(request):
    dict_data = predictor.to_graph(request)
    return HttpResponse(json.dumps(dict_data), content_type='text/json')

def detail_graph_one(request):
    dict_data = predictor.detail_graph_one(request,'layer_10_160_40_180_output')
    return HttpResponse(json.dumps(dict_data), content_type="text/json")

def two_detail_graph_one(request):
    dict_data = predictor.detail_graph_one(request,'layer_160_200_140_300_output')
    return HttpResponse(json.dumps(dict_data), content_type="text/json")

def detail_graph_DR_onevsT(request):
    one_table = ['layer_10_160_40_180_output']
    other_table = ['layer_160_200_140_300_output']
    dict_data = predictor.detail_graph_DR_onevsT(request,one_table, other_table,1)
    return HttpResponse(json.dumps(dict_data), content_type="text/json")

def two_detail_graph_DR_onevsT(request):
    one_table = ['layer_160_200_140_300_output']
    other_table = ['layer_10_160_40_180_output']
    dict_data = predictor.detail_graph_DR_onevsT(request, one_table, other_table,2)
    return HttpResponse(json.dumps(dict_data), content_type="text/json")

def detail_graph_DR_progresses(request):
    dict_data = predictor.detail_graph_DR_progresses(request)
    return HttpResponse(json.dumps(dict_data), content_type="text/json")

def two_to_graph(request):
    dict_data = predictor.two_to_graph(request)
    return HttpResponse(json.dumps(dict_data), content_type='text/json')

def backup(request):
    predictor.to_graph_csv(request)
    t = open("C:/Users/bong/project/semiconductor_project/semiconductor_project/web_server/web/predict/layer_10_160_40_180_output.csv", "r")
    dict_data = t.read()
    t.close()
    print("backup****************************************" )
    return HttpResponse(dict_data, content_type="text/plain")

def two_backup(request):
    predictor.two_to_graph_csv(request)
    t = open("C:/Users/bong/project/semiconductor_project/semiconductor_project/web_server/web/predict/layer_160_200_140_300_output.csv", "r")
    dict_data = t.read()
    t.close()
    print("two_backup****************************************" )
    return HttpResponse(dict_data, content_type="text/plain")

def test_page(request):
    return render(request,'test_page.html')

def goto_test_page(request):
    t = open("C:/Users/bong/project/semiconductor_project/semiconductor_project/web_server/web/predict/layer_10_160_40_180_output_tomain.csv", "r")
    dict_data = t.read()
    t.close()
    print("goto_test_page****************************************" )
    return HttpResponse(dict_data, content_type="text/plain")

def goto_get_quantity(request):
    dict_data = predictor.goto_get_quantity(request, 'layer_10_160_40_180_output')
    return HttpResponse(dict_data, content_type='text/plain')

def two_goto_get_quantity(request):
    dict_data = predictor.goto_get_quantity(request, 'layer_160_200_140_300_output')
    return HttpResponse(dict_data, content_type='text/plain')

def goto_reflec(request):
    predictor.goto_reflec(request, 'layer_10_160_40_180_input', 'layer_10_160_40_180_output')
    t = open("C:/Users/bong/project/semiconductor_project/semiconductor_project/web_server/layer_10_160_40_180_input_X.csv", "r")
    dict_data = t.read()
    t.close()
    return HttpResponse(dict_data, content_type='text/plain')

def two_goto_reflec(request):
    predictor.goto_reflec(request, 'layer_160_200_140_300_input', 'layer_160_200_140_300_output')
    t = open("C:/Users/bong/project/semiconductor_project/semiconductor_project/web_server/layer_160_200_140_300_input_X.csv", "r")
    dict_data = t.read()
    t.close()
    return HttpResponse(dict_data, content_type='text/plain')

def goto_log(request):
    t = open("C:/Users/bong/project/semiconductor_project/semiconductor_project/web_server/web/predict/layer_160_200_140_300_output_tomain.csv", "r")
    dict_data = t.read()
    t.close()
    print("goto_test_page****************************************" )
    return HttpResponse(dict_data, content_type="text/plain")


