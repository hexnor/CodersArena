import base64
import json
import urllib2
from django.http import HttpResponse, JsonResponse

from rest_framework import serializers

from blog.models import Blogs, Categories
from django.shortcuts import render_to_response, get_object_or_404
from django.template import *

def blogindex(request):
    return render_to_response('index.html', {
        'categories': Categories.objects.all(),
        'posts': Blogs.objects.all()[:5],
        'request':request
    })

def view_post(request, post):
    s=Blogs.objects.get(pk=int(post))

    return render_to_response('view_post.html', {
        'post': s, 'request':request
    })

def view_category(request, category):
    return render_to_response('view_category.html', {
        'category': Categories.objects.get(pk=category),
        'posts': Blogs.objects.filter(category=int(category))[:5],
        'request': request
    })


def index(request):
    return render_to_response('index.html', {
        'categories': Categories.objects.all(),
        'posts': Blogs.objects.all()[:5],
        'request':request
    })

from pygithub3 import Github
def project(request):
    gh = Github(user='hexnor',token='cfa654e090102c6b49b43160d4da726ca1f3845b')
    user_repos = gh.repos.list().all()

    all=[]
    for repo in user_repos:
        repos = { 'name':repo.name,
                  'created_at':repo.created_at,
                  'language':repo.language,
                  'description':repo.description,
                  'git_url':repo.git_url,
                  'homepage':repo.homepage

        }
        all.append(repos)
    return render_to_response('projects.html', {
        'request': request,'repos':all
    })
