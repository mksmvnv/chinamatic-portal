# Created by @mksmvnv

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def post(request, post_id):
    return render(request, 'post.html')
