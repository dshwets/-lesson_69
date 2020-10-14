from django.urls import path

from webapp_v2.views import Index_View_v2

app_name = 'webapp_v2'
urlpatterns = [
    path('index/', Index_View_v2.as_view(), name='index')
]