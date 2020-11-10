from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.


#  Ниже в функции news_home приведен пример, того как можно доставать данные из базы данных и использовать их
# в .html страницах. Для этого необходимо создать переменную и присвоить ей ссылку на объект класса Article из
# модели .models и при помощи .objects.all() достать всю информацию. Теперь переменная news содержит ссылку на
# объект с данными из таблицы б/д Article. Затем мы возвращаем страницу news/news_home.html и дополнительным
# параметром, в виде словаря передаем ключь - слово, при помощи которого будут обращаться к данным из файла .html ,
# а в качестве значения передаем переменную со второй строчки


def news_home(request):
	news = Article.objects.all()
	return render(request, 'news/news_home.html', {'news': news[::-1]})


class NewsDetailView(DetailView):
	model = Article
	template_name = 'news/details_view.html'
	context_object_name = 'article'


class NewsUpdateView(UpdateView):
	model = Article
	template_name = 'news/create.html'
	form_class = ArticleForm


class NewsDeleteView(DeleteView):
	model = Article
	success_url = '/news/'
	template_name = 'news/news_delete.html'

# В следующей функции, при обращении к ней, Она проверяет атрибут request, если он не пустой, то идет следующая проверка
# request.method == 'POST', если данная проверка истина, тогда далее следует исполнение первого блока кода и
# соответствующий вывод. Если же request пустой, то первый блок кода не выполняется, а сразу происходит обработка
# блока кода начиная с присвоения переменной form класса АrticleForm(), который мы импортировали из файла .forms
# и в самой последней строке фунуция возвращает запрос, страницу news/create.html и словарь из двух переменных:
# 'form': form, и 'error': error. Соответственно что бы мы могли на странице news/create.html обратиться к этим переменным


def create(request):
	error = ''
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('news_home')
		else:
			error = 'Form wasn\'t filed properly'

	form = ArticleForm()

	data = {
		'form': form,
		'error': error,
	}

	return render(request, 'news/create.html', data)
