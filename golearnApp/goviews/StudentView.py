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
        print(request.session['name'])
        student = BaseTable.Ustudentinfo.objects.get(name=request.session['name'])
        context = {}
        context['yue'] = student.umoney
        return render(request,'studentinfo.html',context);

    @csrf_exempt
    def post(self,request):
        student = BaseTable.Ustudentinfo.objects.get(name=request.session['name'])
        moneysum = request.POST.get('moneysum')
        print(moneysum)
        if (request.POST.get('is_add')== "yes"):
            student.umoney = student.umoney + int(moneysum)
        else:
            student.umoney = student.umoney - int(moneysum)
        student.save()
        hlsdic = {'status':student.umoney}
        response = JsonResponse(hlsdic, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
