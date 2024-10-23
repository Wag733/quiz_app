from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('create-quiz/', views.create_quiz, name='create_quiz'),
    path('quiz/<int:quiz_id>/create-question/', views.create_question, name='create_question'),
    path('question/<int:question_id>/create-specific/', views.create_specific_question, name='create_specific_question'),
    path('quiz/<int:pk>/edit/', views.edit_quiz, name='edit_quiz'),
    path('question/<int:pk>/delete/', views.delete_question, name='delete_question'),
    path('quiz/<int:pk>/delete/', views.delete_quiz, name='delete_quiz'),
    path('quiz/<int:quiz_pk>/question/<int:question_pk>/edit/', views.edit_question, name='edit_question'),
]
