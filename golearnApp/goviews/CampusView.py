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


class CampusView(View):
    '''
    def get(self,request):
        teacher = BaseTable.Uteacherinfo.objects.get(id=request.session['uid'])
        context = {}
        context['user'] = teacher
        campuses = BaseTable.Campus.objects.filter(teacher=teacher)
        context['campuses'] = campuses
        teachers_classes = BaseTable.Teachers_classes.objects.filter(teacher=teacher) 
        context['teachers_classes'] = teachers_classes
        return render(request,'teacherinfo.html',context);
    '''

    @csrf_exempt
    def post(self,request,campusid):
        campus = BaseTable.Campus.objects.get(id=int(campusid))
        logger = logging.getLogger('django')

        logger.error("*****************\n")
        logger.error(request.POST.get("name"))
        logger.error("##################\n")
        logger.error(campus.name)
        logger.error("--------------------\n")
        campus.name=request.POST.get("name"),
        logger.error(campus.name)
        campus.abbreviation=request.POST.get("abbr"),
        campus.stage=request.POST.get("stage"),
        campus.bio=request.POST.get("bio"),
        campus.pupose=request.POST.get("pupose"),

        if request.FILES:
            campus.logo=request.FILES.getlist("logo")[0],
            logger.error(campus.logo)

        logger.error("*****************\n")
        campus.save()
        logger.error("*****************\n")
        result = {'status':"success"}
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
