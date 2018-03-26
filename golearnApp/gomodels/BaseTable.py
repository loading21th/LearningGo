import os
from django.db import  models
from django.db.models import Max

AppPath =  os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
    studentid = Ustudentinfo.objects.all().aggregate(id=Max('id'))['id']
    teacherid = Uteacherinfo.objects.all().aggregate(id=Max('id'))['id']
    if studentid == None and teacherid == None:
        userid = 1
    elif studentid == None:
        userid = teacherid + 1
    elif teacherid == None:
        userid = studentid + 1
    elif studentid > teacherid:
        userid = studentid + 1
    else:
        userid = teacherid + 1
    return userid



class Userinfo(models.Model):
    id=models.AutoField(default=get_id,primary_key=True)
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

    def __str__(self):
        return str(self.id)

class Uteacherinfo(Userinfo):
    uGo_credential = models.ImageField(upload_to=get_image_path)
    uTeach_credential = models.ImageField(upload_to=get_image_path) 
    udescripition = models.TextField() 
    can_createschool = models.BooleanField(default=0) 

    def __str__(self):
        return str(self.id)

class Campus(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    abbreviation = models.CharField(max_length=10) 
    stage = models.IntegerField()
    logo = models.ImageField(upload_to=get_image_path)
    bio = models.TextField()    
    pupose = models.TextField() 
    teacher = models.ForeignKey('Uteacherinfo')
    can_createclass = models.BooleanField(default=0) 

    def __str__(self):
        return str(self.id)

class Classroom(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    abbreviation = models.CharField(max_length=10) 
    stage = models.IntegerField()
    logo = models.ImageField(upload_to=get_image_path)
    bio = models.TextField()    
    time = models.TextField() 
    price = models.IntegerField()
    rtmpaddr = models.CharField(max_length=40)
    campus = models.ForeignKey('Campus')

    def __str__(self):
        return str(self.id)

class Students_classes(models.Model):
    student = models.ForeignKey('Ustudentinfo')
    classroom = models.ForeignKey('Classroom')

    def __str__(self):
        return self.student.name + self.classroom.name


class Teachers_classes(models.Model):
    teacher = models.ForeignKey('Uteacherinfo')
    classroom = models.ForeignKey('classroom')

    def __str__(self):
        return self.teacher.name + self.classroom.name

class Homework(models.Model):
    id=models.AutoField(primary_key=True)
    campus = models.ForeignKey('Campus')
    classroom = models.ForeignKey('Classroom')
    homework = models.FileField(upload_to=get_upfile_path)

    def __str__(self):
        return str(self.id)

class Videos(models.Model):
    stage = models.IntegerField()
    name = models.CharField(max_length=40)
    logo = models.ImageField(upload_to=get_image_path)
    addr = models.FileField(upload_to=get_video_path)

    def __str__(self):
        return self.name
    
