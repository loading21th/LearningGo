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



class AddClassView(View):
    '''
    def get(self,request):
        student = BaseTable.Ustudentinfo.objects.get(id=request.session['uid'])
        hlsdic = {'status':'fail'}
        if ( student.can_upgrade) == "Tru" :
            hlsdic['status'] = 'success'
        response = JsonResponse(hlsdic, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
    '''
    @csrf_exempt
    def post(self,request):
        campus = BaseTable.Campus.objects.get(id=request.session['campusid'])
        rtmp="rtmp://192.168.12.105:1935/"+campus.abbreviation+"/"+request.POST.get("abbr")
        classroom = BaseTable.Classroom(name=request.POST.get('name'),
                                  abbreviation=request.POST.get("abbr"),
                                  stage=request.POST.get("stage"),
                                  bio=request.POST.get("bio"),
                                  time=request.POST.get("time"),
                                  price=request.POST.get("price"),
                                  logo=request.FILES.getlist("logo")[0],
                                  rtmpaddr=rtmp,
                                  campus=campus)
        classroom.save()
        campus.can_createsclass=False
        campus.save()
        hlsdic = {'status':rtmp}
        response = JsonResponse(hlsdic, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
