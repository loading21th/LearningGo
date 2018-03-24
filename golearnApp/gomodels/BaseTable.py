import os
from django.db import  models

AppPath =  os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
userid = 0 

def get_image_path(instance,filename):
    file_path = os.path.join(AppPath,'static','image',instance.name,filename)
    return file_path

def get_upfile_path(instance,filename):
    file_path = os.path.join(AppPath,'uploadfile',instance.Campus.abbreviation,instance.classroom.abbreviation,filename)
    return file_path

def get_video_path(instance,filename):
    file_path = os.path.join(AppPath,'static','videos',filename)
    return file_path

def get_id():
    global userid
    userid = userid + 1
    return userid



class Userinfo(models.Model):
    id = models.IntegerField(default=get_id,primary_key=True)
    name = models.CharField(max_length=40)
    upasswd = models.CharField(max_length=40)
    uemail = models.EmailField(max_length=40)
    ubirth = models.DateField(max_length=40)
    uimage = models.ImageField(upload_to=get_image_path)
    umoney = models.IntegerField()
    usex = models.CharField(max_length=40)
    class Meta:
         abstract = True

class Ustudentinfo(Userinfo):
    can_upgrade = models.BooleanField(default=False)

class Uteacherinfo(Userinfo):
    uGo_credential = models.ImageField(upload_to=get_image_path)
    uTeach_credential = models.ImageField(upload_to=get_image_path) 
    udescripition = models.TextField() 
    can_createschool = models.BooleanField(default=0) 

class Campus(models.Model):
    name = models.CharField(max_length=40)
    abbreviation = models.CharField(max_length=10) 
    stage = models.CharField(max_length=40)
    logo = models.ImageField(upload_to=get_image_path)
    bio = models.TextField()    
    pupose = models.TextField() 
    teacher = models.ForeignKey('Uteacherinfo')
    can_createclass = models.BooleanField(default=0) 

class Classroom(models.Model):
    name = models.CharField(max_length=40)
    abbreviation = models.CharField(max_length=10) 
    teacher = models.CharField(max_length=40) 
    stage = models.IntegerField()
    logo = models.ImageField(upload_to=get_image_path)
    bio = models.TextField()    
    time = models.TextField() 
    price = models.IntegerField()
    rtmpaddr = models.CharField(max_length=40)
    campus = models.ForeignKey('Campus')

class Students_classes(models.Model):
    student = models.ForeignKey('Ustudentinfo')
    classroom = models.ForeignKey('Classroom')


class Teacher_classes(models.Model):
    teacher = models.ForeignKey('Uteacherinfo')
    classroom = models.ForeignKey('classroom')

class Homework(models.Model):
    campus = models.ForeignKey('Campus')
    classroom = models.ForeignKey('Classroom')
    homework = models.FileField(upload_to=get_upfile_path)

class Videos(models.Model):
    stage = models.IntegerField()
    name = models.CharField(max_length=40)
    logo = models.ImageField(upload_to=get_image_path)
    addr = models.FileField(upload_to=get_video_path)
    
