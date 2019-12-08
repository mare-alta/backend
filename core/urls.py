
from django.urls import path
from . import views

urlpatterns = [
    path('Levels/', views.LevelList.as_view()),
    path('Level/', views.LevelDetail.as_view()),
    path('Complaints/', views.ComplaintList.as_view()),
    path('Complaint/', views.ComplaintDetail.as_view()),
]
