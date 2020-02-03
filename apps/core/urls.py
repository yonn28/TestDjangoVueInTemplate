
from django.urls import path
from views import TypeList

urlpatterns = [
    path('', TypeList.as_view()),
]