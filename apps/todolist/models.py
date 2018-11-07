from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username', verbose_name=u'用户')
	event = models.CharField(max_length=20, verbose_name=u'事件')
	describe = models.CharField(max_length=100, verbose_name=u'描述', default='无', blank=True)
	add_time = models.DateTimeField(default=timezone.now,verbose_name=u'添加时间')
	complete = models.BooleanField(default=False, verbose_name=u'是否完成')
	achieve = models.BooleanField(default=True, verbose_name=u'是否生效')
	importance = models.IntegerField(default=0, verbose_name=u'重要性')
	flag = models.IntegerField(choices=((0, 'none'),(1,'red'),(2,'yellow'),(3,'blue'),(4,'green')), default=0, verbose_name=u'旗子标记')
	remind_time = models.DateTimeField(default=timezone.now,verbose_name=u'提醒时间')
	remark = models.CharField(max_length=50, verbose_name=u'备注', blank=True)
	
	class Meta:
		verbose_name = u'代办清单'
		verbose_name_plural = verbose_name
	
	def __str__(self):
		return self.event
	