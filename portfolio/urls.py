"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myportfolio.views import home,portfolio,contact,signup,login,logout_view,terms
from tools.views import toolsPage,studentRslt,calc
from cb.views import cb_signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('portfolio/', portfolio),
    path('contact-me/', contact),
    path('tools/', toolsPage),
    path('student-result/', studentRslt),
    path('calc/', calc),
    path('signup/', signup),
    path('login/', login),
    path('logout/', logout_view),
    path('contact-book/', cb_signup),
    path('terms-and-conditions/', terms),
]
