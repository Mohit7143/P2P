from django.db import models
from django.utils import timezone

# Create your models here.
class look(models.Model):
	ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
	mac = models.CharField(max_length = 25,null=True,blank=True, unique=True)
	time = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return "%s" % self.time

	def __unicode__(self):
		return "%s" % self.mac

class files(models.Model):
	name = models.CharField(max_length=200,unique=True)

	def __str__(self):
		return "%s" % self.name

class record(models.Model):
	file = models.ForeignKey(files,on_delete=models.CASCADE,null=True)
	mac = models.CharField(max_length = 20,null=True,blank=True, unique=False)

	def __str__(self):
		return self.file.name
