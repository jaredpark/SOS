from django.conf.urls import patterns, url
from contact import views

urlpatterns = patterns('',
	url(r'^special-offers/$', views.specials, name = 'specials'),
	url(r'^$', views.contact, name = 'contact'),
)
