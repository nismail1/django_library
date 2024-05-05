from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns = [
    path('books/', views.BookListView.as_view(), name='index'),
]
