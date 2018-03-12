import os
from django.db import  models

AppPath =  os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def get_image_path(instance,filename):
    file_path = os.path.join(AppPath,'image',instance.name,filename)
    return file_path

def get_upfile_path(instance,filename):
    file_path = os.path.join(AppPath,'uploadfile',instance.schoolname,instance.classname,filename)
    return file_path

def get_video_path(instance,filename):
    file_path = os.path.join(AppPath,'goTemplates','videos',filename)
    return file_path



class Ustudentinfo(models.Model):
    name = models.CharField(max_length=40)
    upasswd = models.CharField(max_length=40)
    uemail = models.EmailField(max_length=40)
    ubirth = models.DateField(max_length=40)
    uimage = models.ImageField(upload_to=get_image_path)
    umoney = models.IntegerField()
    usex = models.CharField(max_length=40)
    can_update = models.BooleanField(default=0)

class Uteacherinfo(models.Model):
    name = models.CharField(max_length=40)
    upasswd = models.CharField(max_length=40)
    uemail = models.EmailField(max_length=40)
    ubirth = models.DateField(max_length=40)
    uimage = models.ImageField(upload_to=get_image_path)
    umoney = models.IntegerField()
    usex = models.CharField(max_length=40)
    uGo_credential = models.ImageField(upload_to=get_image_path)
    uTeach_credential = models.ImageField(upload_to=get_image_path) 
    udescripition = models.TextField() 
    can_createschool = models.BooleanField(default=0) 

class campus(models.Model):
    name = models.CharField(max_length=40)
    abbreviation = models.CharField(max_length=10) 
    stage = models.CharField(max_length=40)
    logo = models.ImageField(upload_to=get_image_path)
    bio = models.TextField()    
    pupose = models.TextField() 
    teacher = models.ForeignKey('Uteacherinfo')
    can_createclass = models.BooleanField(default=0) 

class classroom(models.Model):
    name = models.CharField(max_length=40)
    abbreviation = models.CharField(max_length=10) 
    teacher = models.CharField(max_length=40) 
    stage = models.IntegerField()
    logo = models.ImageField(upload_to=get_image_path)
    bio = models.TextField()    
    time = models.TextField() 
    price = models.IntegerField()
    rtmpaddr = models.CharField(max_length=40)
    campus = models.ForeignKey('campus')

class students_classes(models.Model):
    student = models.ForeignKey('Ustudentinfo')
    classroom = models.ForeignKey('classroom')


class teacher_classes(models.Model):
    teacher = models.ForeignKey('Uteacherinfo')
    classroom = models.ForeignKey('classroom')

class homework(models.Model):
    classroom = models.ForeignKey('classroom')
    homework = models.FileField(upload_to=get_upfile_path)

class videos(models.Model):
    stage = models.IntegerField()
    name = models.CharField(max_length=40)
    logo = models.ImageField(upload_to=get_image_path)
    addr = models.FileField(upload_to=get_video_path)
    
