# -*- coding: utf-8 -*-
#!/usr/bin/python

__author__ = 'envisocy'
__date__ = '2018/11/7 17:07'

import xadmin

from .models import *

class TodoListAdmin(object):
	list_display = ['user', 'event', 'describe','add_time', 'complete', 'achieve', 'importance', 'flag', 'remind_time', 'remark']
	search_fields = ['user', 'event', 'describe', 'complete', 'achieve', 'importance', 'flag', 'remark']
	list_filter = ['user', 'event', 'describe', 'add_time', 'complete', 'achieve', 'importance', 'flag', 'remind_time', 'remark']

xadmin.site.register(TodoList, TodoListAdmin)