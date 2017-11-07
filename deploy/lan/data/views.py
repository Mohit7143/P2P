from django.shortcuts import render,redirect
from .models import look,record,files
from django.http import HttpResponse,Http404
from django.views.generic import View
import json
from django.utils import timezone
from django.core import serializers

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def ack(request):
	ip = get_client_ip(request)
	if request.GET.get('mac'):
		try:
			obj = look.objects.get(mac=request.GET.get('mac'))
			look.objects.filter(mac=request.GET.get('mac')).update(ip=ip,time=timezone.now())
		except look.DoesNotExist:
			lk = look()
			lk.ip = ip
			lk.mac = request.GET.get('mac')
			lk.save()
		return HttpResponse(ip)
	else:
		raise Http404("No Such URL exist")

def find(request):
	if request.GET.get('id'):
		cur = files.objects.filter(name=request.GET.get('id'))
		tmp = record.objects.filter(file=cur)
		tm = timezone.now()
		list = []
		for item in tmp:
			row = look.objects.filter(mac=item.mac , time__lte=tm , time__gt=tm-timezone.timedelta(seconds=60)).first()
			if row:
				list.append(row)
		data = serializers.serialize('json',list, fields=('name'))
		return HttpResponse(data, content_type="application/json")
	else:
		raise Http404("No such URL exist")


def get_list(request):
	data = serializers.serialize('json',files.objects.all(), fields=('name'))
	return HttpResponse(data, content_type="application/json")

def download(request):
	if request.GET.get('pid'):
		if request.GET.get('file'):
			pid = request.GET.get('pid')
			seeder = look.objects.get(pk=pid)
			return redirect('http://' + seeder.ip + ':8123/' + request.GET.get('file'))
			pass
		else:
			raise Http404("No such URL exist")
	else:
		raise Http404("No such URL exist")