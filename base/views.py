from django.shortcuts import render
from django.http import HttpResponse


# Template cho việc lưu trữ người dùng
friends = [
    {
        'id': 1,
        'name': 'Nguyen Van B',
        'email': 'vanb@gmail.com'
    },
    {
        'id': 2,
        'name': 'Nguyen Van A',
        'email': 'vana@gmail.com'
    },
    {
        'id': 3,
        'name': 'Nguyen Van C',
        'email': 'vanc@gmail.com'
    }
]

# Template cho việc lưu trữ bài đăng
posts = [
    {
        'author': 'Nguyen Van A',
        'message': 'Hello friends!',
        'author_id': 1,
    },

    {
        'author': 'Nguyen Van B',
        'message': 'Hello everybody',
        'author_id': 2,
    },
]

# Hàm view cho trang web

def loginandregister(request):
    return render(request, 'base/loginandregister.html')

def home(request):
    context = {
        'posts': posts
        }
    return render(request, 'base/home.html', context)

def friendspage(request, pk):
    user = None
    for i in friends: 
        if i['id'] == int(pk):
            user = i 
    context = {'user': user}
    return render(request, 'profile.html', context)
