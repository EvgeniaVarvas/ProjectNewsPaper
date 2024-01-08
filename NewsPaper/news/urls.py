
from django.urls import path
from .views import NewsList, ArticleList, PostDetail, PostCreate, PostUpdate, PostDelete


urlpatterns = [
    path('common_list/news/', NewsList.as_view(), name='news_list'),
    path('common_list/article/', ArticleList.as_view(), name='article_list'),
    path('common_list/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('create_news/', PostCreate.as_view(), name='create_news'),
    path('common_list/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('common_list/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    
    ]

