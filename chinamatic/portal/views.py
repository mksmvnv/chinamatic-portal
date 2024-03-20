# Created by @mksmvnv

from django.shortcuts import render

db_post = [
    {'id': 1, 'title': 'История китайского языка',
        'description': 'Краткое описание'},
    {'id': 2, 'title': 'Здравствуйте на китайском',
        'description': 'Краткое описание'},
]


def index(request):
    context = {
        'posts': db_post,
    }
    return render(request, './portal/index.html', context)


def post(request, post_id):
    context = {
        'post_id': post_id,
    }
    return render(request, './portal/post.html', context)
