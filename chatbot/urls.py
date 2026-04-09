from django.urls import path
from .views import ChatAPIView, index

urlpatterns = [
    path('', index, name='index'),
    path('chat', ChatAPIView.as_view(), name='chat-api'),
]