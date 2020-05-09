from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('record_audio_start/', views.record_audio_start,
         name='record_audio_start'),
    path('record_audio_stop/', views.record_audio_stop, name='record_audio_stop'),
    path('nlp_process/', views.nlp_process, name='nlp_process')
]
