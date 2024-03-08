from django.urls import path
from .views import index, top_sellers, about, task, answer

urlpatterns = [
    path('', index, name='main_page'),
    path('top-sellers/', top_sellers, name='top_sellers'),
    path('about/', about, name='about'),
    path('task/', task, name='task'),
    path('answer/', answer, name='answer')
]
