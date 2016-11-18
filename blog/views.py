from django.shortcuts import render
from django.utils import timezone

posts=[
    {
    'id':1,	
    'title': 'post1',
    'published_date': '1.01.2015',
    'author':'vasya',
    'comments': 15
    },
    {
   	'id':2,
        'title': 'post2',
        'published_date': '20.09.2015',
        'author': 'dima',
        'comments': 30
    },
    {
	'id':3,
        'title': 'post3',
        'published_date': '11.03.2015',
        'author': 'dasha',
        'comments': 100
    },
    {
        'id':4,
        'title': 'post4',
        'published_date': '30.05.2015',
        'author': 'dima',
        'comments': 2
    },
    {
        'id':5,
        'title': 'post5',
        'published_date': '1.10.2014',
        'author': 'masha',
        'comments': 20
    },
    {
        'id':6,
        'title': 'post6',
        'published_date': '1.01.2015',
        'author': 'vasya',
        'comments': 25
    },
    ]

def post_list(request):
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = posts[int(pk)-1]	
    return render(request, 'blog/post_detail.html', {'post': post})