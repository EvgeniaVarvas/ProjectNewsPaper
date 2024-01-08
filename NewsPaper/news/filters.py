from .models import Post
from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput


# class PostFilter(FilterSet):
#     added_after = DateTimeFilter(
#         field_name='created',
#         lookup_expr='gt',
#         widget=DateTimeInput(
#             format='%Y-%m-%dT%H:%M',
#             attrs={'type': 'datetime-local'},
#         ),
#     )
#     class Meta:
#         model = Post
#         fields = {
#             'name': ['icontains'],
#         }

# class PostFilter(FilterSet):
# class PostFilter(FilterSet):
#     class Meta:
#         model = Post
#         fields = '__all__'
#         labels = {
#             'post_type': 'Тип поста',
#             'created': 'Дата создания',
#             'categories': 'Категории',
#             'title': 'Заголовок',
#             'text': 'Текст',
#             'rating': 'Рейтинг',
#         }

class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='created',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }
       