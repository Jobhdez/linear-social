from django.urls import path
from . import views


app_name = 'chat'


urlpatterns = [
    path('room/<int:study_id>/', views.study_chat_room,
         name='course_chat_room'),
]
