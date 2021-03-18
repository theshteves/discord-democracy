from django.urls import path

from democracy import views

app_name = 'democracy'
urlpatterns = [
    path('', views.index, name='index'),
    path('<route>', views.other, name='other'),
]
