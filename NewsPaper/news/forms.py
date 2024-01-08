from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    # categories = forms.ModelChoiceField(
    #     queryset=Category.objects.all().values_list('name', flat=True),
    #     label = 'Категория',)
    class Meta:
        model = Post
        fields = ['title', 'text', 'post_type']
        labels = {
            'title': 'Заголовок',  
            'text': 'Текст',       
            'post_type': 'Тип поста', 
            
        }
