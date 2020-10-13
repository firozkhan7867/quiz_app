from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login', views.login, name='login'),
    path('instruction',views.instruction,name='instruction'),
    path('quiz',views.quiz,name="quiz"),
    path('results', views.results, name="results")
]
