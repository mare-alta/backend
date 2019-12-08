
from django.urls import path
from . import views

urlpatterns = [
    path('levels/', views.LevelList.as_view()),
    path('level/', views.LevelDetail.as_view()),
    path('complaints/', views.ComplaintList.as_view()),
    path('complaint/', views.ComplaintDetail.as_view()),
    path('answers/', views.AnswerList.as_view()),
    path('answer/', views.AnswerDetail.as_view()),
]
