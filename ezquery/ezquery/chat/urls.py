from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('audio_to_text/', views.audio_to_text, name='audio_to_text')
]
