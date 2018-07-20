# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Album
from django.http import Http404

# Create your views here.
def index(request):
	all_albums = Album.objects.all()
	# html = ''
	# for album in all_albums:
	# 	url = '/music/' + str(album.id) + '/'
	# 	html += '<a href = "' + url + '">' + album.album_title + '</a><br>'
	# context = {'all_albums': all_albums,}
	return render(request, 'music/index.html', {'all_albums': all_albums,})


def detail(request, album_id):
	try:
		album = Album.objects.get(pk = album_id)
	except Album.DoesNotExist:
		raise Http404('Album does not exist')
	return render(request, 'music/detail.html', {'album': album})

