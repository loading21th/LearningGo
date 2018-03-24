
from django.contrib import admin
from golearnApp.gomodels.BaseTable import Ustudentinfo 
from golearnApp.gomodels.BaseTable import Uteacherinfo 
from golearnApp.gomodels.BaseTable import Campus 
from golearnApp.gomodels.BaseTable import Classroom 
from golearnApp.gomodels.BaseTable import Students_classes 
from golearnApp.gomodels.BaseTable import Teacher_classes 
from golearnApp.gomodels.BaseTable import Homework 
from golearnApp.gomodels.BaseTable import Videos 

admin.site.register(Ustudentinfo)
admin.site.register(Uteacherinfo)
admin.site.register(Campus)
admin.site.register(Classroom)
admin.site.register(Students_classes)
admin.site.register(Teacher_classes)
admin.site.register(Homework)
admin.site.register(Videos)
# Register your models here.
