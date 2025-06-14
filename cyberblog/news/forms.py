from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    author_name = forms.CharField(
        label='Ваше имя',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваше имя'
        })
    )

    class Meta:
        model = News
        fields = ['title', 'content', 'image', 'source']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок новости'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Введите содержание новости'
            }),
            'source': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите источник новости'
            }),
        }
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'image': 'Изображение',
            'source': 'Источник',
        } 