from django.urls import path

from api_v1.views import get_token_view, ArticleCreateView, AddView

app_name = 'api_v1'

urlpatterns = [
    path('get-token/', get_token_view, name='get_token'),
    path('article-create/', ArticleCreateView.as_view(), name='article_create'),
    path('add/', AddView.as_view(), name='add'),
    path('subtract/', AddView.as_view(), name='subtract'),
    path('multiply/', AddView.as_view(), name='multiply'),
    path('divide/', AddView.as_view(), name='divide'),
]
