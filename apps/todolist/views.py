from django.shortcuts import render, HttpResponse, redirect
from .models import TodoList
from django.utils import timezone


# Create your views here.

def TodolistView(request):
	if request.user.is_authenticated:
		try:
			todolists = TodoList.objects.filter(achieve=1, user_id=request.user).all().order_by('complete', '-remind_time')
		except:
			todolists = {}
		return render(request, "todolist/todolist.html", {'todolists': todolists})
	else:
		return render(request, "todolist/unopened.html")

def TodolistSubmitView(request):
	if request.method == 'POST':
		# 取出数据
		id = request.POST.get('id')
		event = request.POST.get('event')
		describe = request.POST.get('describe')
		importance = request.POST.get('importance')
		flag = request.POST.get('flag')
		remind_time = request.POST.get('remind_time')
		remark = request.POST.get('remark')
		user_id = request.POST.get('user_id')
		# 存储数据
		if id != '0':
			TodoList.objects.filter(id=id).update(
				event = event,
				describe = describe,
				importance = importance,
				flag = flag,
				remind_time = remind_time,
				remark = remark,
			)
		else:
			TodoList.objects.create(
				event = event,
				describe = describe,
				importance = importance,
				flag = flag,
				remind_time = remind_time,
				remark = remark,
				user_id = user_id,
				add_time = timezone.datetime.now(),
				complete = 0,
				achieve = 1,
			)
		return render(request, 'todolist/todolist.html')
	else:
		return render(request, 'todolist/todolist.html')

def TodolistCheckedView(request):
	if request.method == 'POST':
		id = request.POST.get('id')
		done = request.POST.get('done')
		TodoList.objects.filter(id=id).update(
			complete = done.capitalize(),
		)
	return HttpResponse(200)

def TodolistDeleteView(request):
	if request.method == "POST":
		id = request.POST.get('id')
		TodoList.objects.filter(id=id).update(
			achieve = 0,
		)
	return HttpResponse(200)

def RecycleView(request):
	try:
		todolists = TodoList.objects.filter(achieve=0, user_id=request.user).all().order_by('complete', '-remind_time')
	except:
		todolists = {}
	return render(request, "todolist/recycle.html", {'todolists': todolists})

def TodolistRecoveryView(request):
	if request.method == "POST":
		id = request.POST.get('id')
		TodoList.objects.filter(id=id).update(
			achieve = 1,
		)
	return HttpResponse(200)
