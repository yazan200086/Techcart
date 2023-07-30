from django.urls import path
from . import views


urlpatterns = [
    path('test', views.get_answers_class.as_view())
]

