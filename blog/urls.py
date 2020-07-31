from django.urls import path
from . import views

urlpatterns = [
    path('',views.list,name='listpost'),
    path('<int:id>/',views.post,name='detailpost'),
]
