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



class AddCampusView(View):
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
        teacher = BaseTable.Uteacherinfo.objects.get(id=request.session['uid'])
        logger = logging.getLogger('django')
        logger.error(request.POST.get('name'))
        campus = BaseTable.Campus(name=request.POST.get('name'),
                                  abbreviation=request.POST.get("abbr"),
                                  stage=request.POST.get("stage"),
                                  bio=request.POST.get("bio"),
                                  pupose=request.POST.get("pupose"),
                                  logo=request.FILES.getlist("logo")[0],
                                  teacher=teacher,
                                  can_createclass=False)
        logger.error(campus.name)
        campus.save()
        teacher.can_createschool=False
        teacher.save()
        hlsdic = {'status':'success'}
        response = JsonResponse(hlsdic, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
