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



class TeacherView(View):
    def get(self,request):
        teacher = BaseTable.Uteacherinfo.objects.get(id=request.session['uid'])
        context = {}
        context['user'] = teacher
        campuses = BaseTable.Campus.objects.filter(teacher=teacher)
        context['campuses'] = campuses
        teachers_classes = BaseTable.Teachers_classes.objects.filter(teacher=teacher) 
        context['teachers_classes'] = teachers_classes
        return render(request,'teacherinfo.html',context);

    @csrf_exempt
    def post(self,request):
        teacher = BaseTable.Uteacherinfo.objects.get(id=request.session['uid'])
        name = request.POST.get('name')
        email = request.POST.get('email')
        birth = request.POST.get('birth')
        sex = request.POST.get('sex')

        if request.FILES:
            image = request.FILES.getlist('image')[0]
            teacher.uimage = image

        teacher.name = name
        teacher.uemail = email
        teacher.ubirth = birth
        teacher.usex = sex

        teacher.save()
        result = {'status':"success"}
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
