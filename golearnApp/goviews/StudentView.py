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



class StudentView(View):
    def get(self,request):
        student = BaseTable.Ustudentinfo.objects.get(id=request.session['uid'])
        context = {}
        context['user'] = student
        logo = os.path.join('/static','image',student.name,os.path.basename(student.uimage.url))
        context['logo'] = logo
        students_classes = BaseTable.Students_classes.objects.filter(student=student) 
        context['students_classes'] = students_classes
        return render(request,'studentinfo.html',context);

    @csrf_exempt
    def post(self,request):
        student = BaseTable.Ustudentinfo.objects.get(id=request.session['uid'])
        name = request.POST.get('name')
        email = request.POST.get('email')
        birth = request.POST.get('birth')
        sex = request.POST.get('sex')

        if request.FILES:
            image = request.FILES.getlist('image')[0]
            student.uimage = image

        student.name = name
        student.uemail = email
        student.ubirth = birth
        student.usex = sex

        student.save()
        result = {'status':"success"}
        response = JsonResponse(result, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
