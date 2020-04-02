from django.conf.urls import url
from django.urls import include, path

from .import views

app_name = 'website'

urlpatterns = [
	path('', views.index, name="index"),
	path('casino-bonus/', views.bonus_page, name="bonus_page"),
	path('casino-spel-slots/', views.casino_spel, name="casino_spel"),
	path('om-oss/', views.omOss, name="omOss"),
	path('artikel-<slug>/', views.article_page, name="article_page"),
]