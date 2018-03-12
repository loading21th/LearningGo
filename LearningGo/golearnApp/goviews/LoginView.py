# coding:utf-8
from django.shortcuts import render
from django.views.generic import View

from django.http import HttpResponse
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
import os 
import json



class LoginView(View):
    def get(self,request):
        return render(request,'login.html');
'''    
    @csrf_exempt
    def post(self,request,school_name,class_name):
        upload_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),'uploadfile',school_name,class_name)
        print(upload_path)

        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        if request.FILES:
            print ('**********add data*********')
            file_obj = request.FILES.getlist('filename')[0]
            hh = Homewore_Courseware(schoolname=school_name,classname=class_name,homework=file_obj)
            hh.save()
            print ('**********save over*********')

        hlsdic = {'Courseware_name':os.listdir(upload_path)}
        response = JsonResponse(hlsdic, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
'''
