from django.urls import path
from .views import VoiceAssistantAPIView

urlpatterns = [
    path('process-voice/', VoiceAssistantAPIView.as_view(), name='voice-process'),
]