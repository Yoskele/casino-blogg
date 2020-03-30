from django.db import models
from django_bleach.models import BleachField
# Create your models here.

class Casino_supplier(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(default=None, blank=True, null=True)
	bonus = BleachField(blank=True, null=True)
	link = BleachField(blank=True, null=True)
	warning_label = BleachField(blank=True, null=True)
	position = models.IntegerField(blank=True, default=500)

	def __str__(self):
		return '{}'.format(
			self.name,
		)
class Article(models.Model):
	slug = models.SlugField(blank=True)
	name = models.CharField(max_length=200, blank=True)
	image = models.ImageField(default=None, blank=True, null=True)
	intro_text = BleachField(blank=True)
	content = BleachField(blank=True)
	link = BleachField(blank=True)
	date = models.CharField(max_length=200, blank=True)
	automated_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}'.format(
			self.name
		)