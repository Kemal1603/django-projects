from django.shortcuts import render


# Create your views here.


def index(request):
	return render(request, 'mainApp/home_page.html')


# В файле webexample/views.py метод index мы реализовывали при помощи запросов
# HttpResponse? что в свою очередь можно, но не совсем правильно, наиболее верный способ
# это применение метода render для возможности использования, так называемого
# шаблонизатора JinJa. Функция index обязательно должна принимать аргумент request,
# а так же в методе render первым аргументом обязательно  нужно указать тот же самый
# request, вторым аргументом в render передаем путь до того фала .html который мы хотим
# вернуть при обращении  к данной функции. ВАЖНОЕ ЗАМЕЧАНИЕ!!! При написпнии
# вышеуказанной функции Джанго по умолчанию ищет папку под названием templates в
# локальной дирректории и начинает подтягивать .html- файлы из этой папки. В связи с
# этим по умолчанию, можно было бы в качестве второго аргумента, метода render передать
# home_page.html однако из-за того, что Джанго собирает все файлы из папок всех
# приложений templates одном месте, для исполнения, ТО РЕКОМЕНДУЕТСЯ В дирректориях
# templates всех приложений создавать внутренние папки с названием приложений, так как
# в этом случае Джанго будет собирать все .html-файлы с их "НАДПАПКАМИ" и таким образом
# можно будет избежать ПОТЕНЦИАЛЬНОГО КОНФЛИКТА ИМЕН, то есть если мы вторым параметром
# указываем mainApp/home_page.html - это означает, что полный путь файла, до которого
# мы хотим обратиться: dudarev/mainApp/templates/mainApp/home_page.html
# P.S.
# Использование шаблонизатор JinJa будет происходи непосредственно в самих файлах .html


def contact(request):
	return render(request, 'mainApp/basic.html', {'values': ['For any assistance please contact me', '+375298575940']})
