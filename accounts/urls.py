from django.urls import path
from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'accounts'

urlpatterns = [
	path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
]