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



class ClassroomView(View):
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
    def post(self,request,classroomid):
        classroom = BaseTable.Classroom.objects.get(id=int(classroomid))

        name=request.POST.get('name'),
        abbreviation=request.POST.get('abbr'),
        stage=request.POST.get('stage'),
        bio=request.POST.get('bio'),
        time=request.POST.get('time'),
        price=request.POST.get('price'),

        if request.FILES:
            logo=request.FILES.getlist("logo")[0],
            classroom.logo=logo

        classroom.name = name
        classroom.abbreviation = abbreviation
        classroom.stage = int(stage)
        classroom.bio = bio
        classroom.time = time
        classroom.price = int(price)
        rtmp="rtmp://192.168.12.105:1935/"+classroom.campus.abbreviation+"/"+abbreviation
        classroom.rtmpaddr = rtmp

        classroom.save()
        result = {'status':"success"}
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
