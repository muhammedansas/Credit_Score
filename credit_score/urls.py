from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.question_view, name='questions'),
    path('submit-answer/', views.submit_answer, name='submit_answer'),
    path('results/', views.results_view, name='results_view'),
]