from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticleForm(ModelForm):
	class Meta:
		model = Article
		# Ключевое слово fields используется для того, чтобы указывать в качестве значения-список тех полей,
		# которые мы бы хотели отображать на странице с формой, для добавления НОВОСТИ create.html
		fields = ['title', 'anons', 'full_text', 'date']

		# Для добавления атрибутов к каждому элементу из базы, в python используется отдельный словарь widgets
		# Делается это для функциональности, иначе форма работать не будет. Прописываем то же самое, как если бы
		# прописывали разметку .html, только вместо разметки словарь, где ключом являются названия полей, а в качестве
		# значений ключей передаем вид инпута, который мы хотим видеть и в качестве аттрибута инпута передаем ключевое
		# слово attrs, который в свою очередь состоит из словаря вида: наименование аттрибута и его значение Например:

		widgets = {
			'title': TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'News Title'
			}),
			'anons': TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Anons'
			}),
			'date': DateTimeInput(attrs={
				'class': 'form-control',
				'placeholder': 'Publish Date'
			}),
			'full_text': Textarea(attrs={
				'class': 'form-control',
				'placeholder': 'News Text'
			})
		}
