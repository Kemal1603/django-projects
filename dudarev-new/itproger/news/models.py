from django.db import models

# Create your models here.


class Article(models.Model):
	title = models.CharField('Title', max_length=50)
	anons = models.CharField('Anons', max_length=250)
	full_text = models.TextField('Article')
	date = models.DateTimeField('Publish date')

	# Этот класс специально придуман, для того, что бы фиксить баг в панели администрирования
	# так как без этого класса, если бы например наш основной класс назывался Articles, то в панели админа
	# название выводилось бы как Articless, так как джанго сам по себе в конце добавляет s к любому слову
	# а так, через класс Meta мы сообшаем, что в единственном числе verbose_name наш класс будет читаться Article,
	# а во множественном verbose_name_plural - Articles. При этом в панели будет отображаться именно то, что мы
	# укажем в классе Meta, то есть даже если класс будет называться Article, а в Meta мы укажем verbose_name = 'абвг',
	# то в панели будет выведено абвг

	def get_absolute_url(self):
		return f'/news/{self.id}'

	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'

	def __str__(self):
		return self.title


