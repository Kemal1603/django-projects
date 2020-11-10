from django.conf.urls import url
from . import views


urlpatterns = [

	url('contact/', views.contact, name='contact'),
	url('', views.index, name='index')
]
