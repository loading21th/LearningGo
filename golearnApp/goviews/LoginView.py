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
import logging



class LoginView(View):
    def get(self,request):
        return render(request,'login.html');

    @csrf_exempt
    def post(self,request):
        name = request.POST.get('name')
        result = {'status':'fail'}
        users =  BaseTable.Ustudentinfo.objects.filter(name=name)
        if not users.exists():
            users = BaseTable.Uteacherinfo.objects.filter(name=name)
        if users.exists():
            if ( (request.POST.get('passwd')) == users[0].upasswd ):
                request.session['uid']=users[0].id
                result['status'] = 'success'
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
