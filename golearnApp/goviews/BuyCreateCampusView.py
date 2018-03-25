# coding:utf-8
from django.shortcuts import render
from django.views.generic import View

from django.http import HttpResponse
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
from golearnApp.gomodels import BaseTable
import os 
import json



class BuyCreateCampusView(View):
    def get(self,request):
        teacher = BaseTable.Uteacherinfo.objects.get(id=request.session['uid'])
        hlsdic = {'status':'fail'}
        if teacher.can_createschool:
            hlsdic['status'] = 'success'
        response = JsonResponse(hlsdic, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response

    @csrf_exempt
    def post(self,request):
        teacher = BaseTable.Uteacherinfo.objects.get(id=request.session['uid'])
        nowmoney = teacher.umoney
        money_update_sum = 100
        stat = "操作失败，请重试"

        if (request.POST.get('is_add')== "createcampus"):
            nowmoney = nowmoney - int(money_update_sum)

        if nowmoney < 0:
            stat = "购买失败，余额不足"
        else:
            stat = "success"
            teacher.umoney = nowmoney
            teacher.can_createschool  = True
            teacher.save()
        result = {'status':stat}
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
