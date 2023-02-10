from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('confesion/', views.Confession.as_view(), name='confession'),
    path('biblia/', views.Bible.as_view(), name='bible'),
]
