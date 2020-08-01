from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostListView.as_view(),name='listpost'),
    path('<int:pk>/',views.PostDetailView.as_view(),name='detailpost'),# pk is primary key
]
