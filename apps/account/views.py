from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def IndexView(request):
	return render(request, 'index.html')

def SigninView(request):
	if request.method == 'GET':
		return render(request, 'account/signin.html')
	elif request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		try:
			User.objects.get(username=username)
			user_name = auth.authenticate(username=username, password=password)
			if user_name == None:
				return render(request, 'account/signin.html', {"warning": "用户名或密码输入错误！"})
			else:
				auth.login(request, user_name)
				return redirect('主页')
		except:
			return render(request, 'account/signin.html', {"warning": "该用户不是有效的注册用户！"})

def SignupView(request):
	return render(request, 'account/signup.html')

def SignoutView(request):
	auth.logout(request)
	return redirect('主页')

@login_required
def AccountView(request):
	usermessage = User.objects.get(username=request.user)
	return render(request, "account/information.html", {"usermessage": usermessage})