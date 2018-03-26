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


class IndexView(View):
    def get(self,request):
        users =  BaseTable.Ustudentinfo.objects.filter(id=request.session['uid'])
        result={"user":"student"}
        if not users.exists():
            users = BaseTable.Uteacherinfo.objects.filter(id=request.session['uid'])
            result["user"] = "teacher"
        return render(request,'index.html',result);
    
    @csrf_exempt
    def post(self,request):
        hlsdic = {'status':'success'}
        response = JsonResponse(hlsdic, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response

