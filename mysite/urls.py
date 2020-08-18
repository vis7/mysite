"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic.base import TemplateView

from polls.views import IndexView

urlpatterns = [
    # path('', IndexView.as_view(), name='home'), # home for polls
	path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    # login views
    # path('login/', auth_views.login, name='login'),
    # chcek this bellow diffrent style
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    # password reset
    # url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # accounts
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),    
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # home for authentication
]
