from django.urls import path
from .views import HomeView, ContactMessageView, AIAssistantView

app_name = 'portfolio'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/contact/', ContactMessageView.as_view(), name='contact_api'),
    path('api/ai-assistant/', AIAssistantView.as_view(), name='ai_assistant_api'),
]
