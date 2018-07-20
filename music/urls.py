from django.conf.urls import url
from . import views

app_name = 'music'
urlpatterns = [
	# /music/ matches to the home page.
	url(r'^$', views.index, name = 'index'),

	# /music/id/
	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name = 'detail'),

	# /music/id/favourite/
	url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name = 'favourite'),

]