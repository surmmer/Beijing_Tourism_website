import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import urllib.parse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages



from django.shortcuts import render
from django.http import JsonResponse

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Invalid username or password.'})

        # 用户名和密码匹配成功
        return redirect('index')

    return render(request, 'sign_in.html')




def sign_up(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if not email:
            error_message = '注册失败，邮箱地址不能为空。'
        else:
            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                error_message = '注册失败，该用户名已被使用。'
            elif User.objects.filter(email=email).exists():
                error_message = '注册失败，该邮箱地址已被使用。'
            else:
                user = User.objects.create(username=username, password=password, email=email)
                messages.success(request, '注册成功！')
                return redirect('sign_in')  # Redirect to sign in page after successful registration

        # Redirect back to sign up page with error message
        query_string = f'?error={urllib.parse.quote(error_message)}'
        return HttpResponseRedirect('/sign_up/' + query_string)

    return render(request, 'sign_up.html')


def index(request):
    return render(request, 'index.html')


def information(request):
    return render(request, 'information.html')


def scenery(request):
    return render(request, 'scenery.html')


def food(request):
    return render(request, 'food.html')


