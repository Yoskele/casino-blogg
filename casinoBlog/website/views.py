from django.shortcuts import render, redirect
from .models import Casino_supplier, Article

def index(request):
	casino_suppliers = Casino_supplier.objects.all()
	articles = Article.objects.all().order_by('-date')[:4]
	context = {
		'casino_suppliers':casino_suppliers,
		'articles':articles,
	}
	return render(request, 'index.html', context)
def bonus_page(request):
	casino_suppliers = Casino_supplier.objects.all()
	articles = Article.objects.filter().order_by('-date')[4:8]
	context = {
		'articles':articles,
		'casino_suppliers':casino_suppliers,
	}
	return render(request, 'bonus_page.html', context)
def casino_spel(request):
	casino_suppliers = Casino_supplier.objects.all()
	articles = Article.objects.filter().order_by('-date')[8:12]
	context = {
		'articles':articles,
		'casino_suppliers':casino_suppliers,
	}
	return render(request, 'casino_spel.html', context)
def article_page(request, slug):
	article = Article.objects.get(slug=slug)
	print(article.id)
	all_articles = Article.objects.all().exclude(id = article.id).order_by('-date')[:4]
	context = {
		'article':article,
		'all_articles':all_articles,
	}
	return render(request, 'article_page.html', context)
def omOss(request):
	return render(request, 'omOss.html')