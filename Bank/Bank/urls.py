"""Bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from login.views import Home,Login,Logout,Auth_user,Loggedin,Invalid_login,UserFormView,SaveProfile,My_transactions
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',Home),
    url(r'^login/',Login),
    url(r'^logout/',Logout),
    url(r'^auth/',Auth_user),
    url(r'^loggedin/',Loggedin),
    url(r'^invalid/',Invalid_login),
    url(r'^signup/',UserFormView.as_view()),
    
    url(r'^saved/', SaveProfile),
    url(r'^mytrans/',My_transactions),
]
