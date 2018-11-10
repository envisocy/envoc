from django.shortcuts import render
from .models import TodoList

# Create your views here.

def TodolistView(request):
	try:
		todolists = TodoList.objects.filter(achieve=1, user_id=request.user).all().order_by('-remind_time')
	except:
		todolists = {}
	return render(request, "todolist/todolist.html", {'todolists': todolists})

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
		# 存储数据
		TodoList.objects.filter(id=id).update(
			event=event,
			describe=describe,
			importance=importance,
			flag=flag,
			remind_time=remind_time,
			remark=remark,
		)
		return render(request, 'todolist/todolist.html')
	else:
		return render(request, 'todolist/todolist.html')