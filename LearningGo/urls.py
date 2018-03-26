"""LearningGo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls)),
"""
from django.conf.urls import url
from django.contrib import admin
from golearnApp.goviews import IndexView
from golearnApp.goviews import RegisterView
from golearnApp.goviews import LoginView
from golearnApp.goviews import StudentView
from golearnApp.goviews import TeacherView
from golearnApp.goviews import BuyUpgradeView
from golearnApp.goviews import UpgradeinfoView
from golearnApp.goviews import WalletView
from golearnApp.goviews import BuyCreateCampusView
from golearnApp.goviews import BuyCreateClassView
from golearnApp.goviews import AddClassView
from golearnApp.goviews import AddCampusView
from golearnApp.goviews import ManageCampusView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^LearningGo/register.html', RegisterView.RegisterView.as_view()),
    url(r'^LearningGo/login.html', LoginView.LoginView.as_view()),
    url(r'^LearningGo/index.html',IndexView.IndexView.as_view()),
    url(r'^LearningGo/userinfo/student',StudentView.StudentView.as_view()),
    url(r'^LearningGo/userinfo/buyupgrade',BuyUpgradeView.BuyUpgradeView.as_view()),
    url(r'^LearningGo/userinfo/upgradeinfo',UpgradeinfoView.UpgradeinfoView.as_view()),
    url(r'^LearningGo/userinfo/teacher',TeacherView.TeacherView.as_view()),
    url(r'^LearningGo/userinfo/wallet',WalletView.WalletView.as_view()),
    url(r'^LearningGo/userinfo/buycreatecampus',BuyCreateCampusView.BuyCreateCampusView.as_view()),
    url(r'^LearningGo/userinfo/buycreateclass',BuyCreateClassView.BuyCreateClassView.as_view()),
    url(r'^LearningGo/userinfo/addcampus',AddCampusView.AddCampusView.as_view()),
    url(r'^LearningGo/userinfo/addclass',AddClassView.AddClassView.as_view()),
    url(r'^LearningGo/campus/manage/(?P<campusid>\d+)',ManageCampusView.ManageCampusView.as_view()),
    ]
'''
    url(r'^LearningGo/index/videos/(?P<stage>\d+)',FindVideosView.FindVideosView.as_view()),
    url(r'^LearningGo/index/campuses/(?P<stage>\d+)',FindCampusesView.FindCampusesView.as_view()),
    url(r'^LearningGo/campus/(?P<campus_name>.*)',CampusView.CampusView.as_view()),
    url(r'^LearningGo/campus/buyclass/(?P<campus_name>.*)/(?P<class_name>)/',BuyClassView.BuyClassView.as_view()),
    url(r'^LearningGo/hlsroom/(?P<campus_name>.*)/(?P<class_name>)/',HlsRoomView.HlsRoomView.as_view()),
    url(r'^LearningGo/hlsroom/homework_upload/(?P<campus_name>.*)/(?P<class_name>)/',HomeworkUpView.HomeworkUpView.as_view()),
    url(r'^LearningGo/hlsroom/courseware_download/(?P<campus_name>.*)/(?P<class_name>)/',CoursewareDownView.CoursewareDownView.as_view()),
    url(r'^LearningGo/userinfo/student',StudentView.StudentView.as_view()),
    url(r'^LearningGo/userinfo/updateinfo',UpdateinfoView.UpdateinfoView.as_view()),
    url(r'^LearningGo/userinfo/delclass/(?P<class_room>)',DelClassView.DelClassView.as_view()),
    url(r'^LearningGo/userinfo/updateclass/(?P<campus_name>.*)/(?P<class_name>)/',UpdateClassView.UpdateClassView.as_view()),
    url(r'^LearningGo/userinfo/teacherdelClass/(?P<campus_name>.*)/(?P<class_name>)/',TeacherDelClassView.TeacherDelClassView.as_view()),
'''
