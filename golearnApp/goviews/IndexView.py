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
        result={"user":"student"}
        if request.session['uid'] > 99999:
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

