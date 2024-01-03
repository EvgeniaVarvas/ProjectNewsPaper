
from django.urls import path
from .views import NewsList, NewsDetail



# urlpatterns = [
#     path('news/', NewsList.as_view(), name='news_list'),
#     path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),

#     path('articles/', ArticleListView.as_view(), name='article_list'),
    # path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
# ]
urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
   
    ]
