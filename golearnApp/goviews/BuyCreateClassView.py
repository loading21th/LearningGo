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



class BuyCreateClassView(View):
    def get(self,request):
        teacher = BaseTable.Uteacherinfo.objects.get(id=request.session['uid'])
        campus_name = request.GET['campus_name']
        campuses= BaseTable.Campus.objects.filter(name=campus_name,teacher=teacher)
        hlsdic = {'status':'fail'}
        if campuses.exists():
            campus = campuses[0]
            if campus.can_createclass:
                hlsdic['status'] = 'success'
            request.session['campusid']=campus.id
        response = JsonResponse(hlsdic, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response

    @csrf_exempt
    def post(self,request,campus):
        teacher = BaseTable.Uteacherinfo.objects.get(id=request.session['uid'])
        campus = BaseTable.Campus.objects.get(id=request.session['campusid'])
        nowmoney = teacher.umoney
        money_update_sum = 100
        stat = "操作失败，请重试"

        if (request.POST.get('is_add')== "createclass"):
            nowmoney = nowmoney - int(money_update_sum)

        if nowmoney < 0:
            stat = "购买失败，余额不足"
        else:
            stat = "success"
            teacher.umoney = nowmoney
            campus.can_createclass  = True
            teacher.save()
            campus.save()
        result = {'status':stat}
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
