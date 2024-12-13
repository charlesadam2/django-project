from django.urls import path
from health import views

app_name='health'

urlpatterns=[
	path('', views.index, name='index'),
    path('contact/list/', views.contact_list, name='contact_list'),
	]