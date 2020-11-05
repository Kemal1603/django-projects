from django.db import models
from datetime import date


# Create your models here.
class Category(models.Model):
    """Описываем поля таблицы, то есть столбцы"""

    name = models.CharField('Category', max_length=150)

    #  TextField() - Текстовое поле, в котором не указываются ограничения

    description = models.TextField('Description')

    #  SlugField - ткестовое поле, в котором пропис   ываются: Буквы, Цифры, Подчеркивания и дефисы

    url = models.SlugField(max_length=160, unique=True)

    # Метод __str__ нужен для возврата модели в строковом представлении

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'


class Actor(models.Model):
    name = models.CharField('Name', max_length=100)
    age = models.PositiveSmallIntegerField('Age', default=0)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actors and directors'
        verbose_name_plural = 'Actors and directors'


class Genre(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genre'


class Movie(models.Model):
    title = models.CharField('Name', max_length=100)
    tag_line = models.CharField('Slogan', max_length=100, default='')
    description = models.TextField('Description')
    poster = models.ImageField('Image', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Year', default=2019)
    country = models.CharField('Country', max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name='Director', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='Actors', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='genre')
    world_premier = models.DateField('World premiere', default=date.today)
    budget = models.PositiveIntegerField('Budget', default=0, help_text='write sum in USD')
    fees_in_USA = models.PositiveIntegerField('Collected in USA', default=0, help_text='write sum in USD')
    fees_in_world = models.PositiveIntegerField('Collected in world', default=0, help_text='write sum in USD')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Draft', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movies'
        verbose_name_plural = 'Movies'


class MovieShots(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description')
    image = models.ImageField('Images', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Movie', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Shots from film'
        verbose_name_plural = 'Shots from film'


class RatingStar(models.Model):
    value = models.SmallIntegerField('Value', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Star rating'
        verbose_name_plural = 'Star rating'


class Rating(models.Model):
    ip = models.CharField('IP address', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='star')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='film')

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Rating'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Name', max_length=100)
    text = models.TextField('Message', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='parent', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='film', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Review'

