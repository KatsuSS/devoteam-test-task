from django.urls import path

from .views import UserCommunications, GraphCommunication


urlpatterns = [
    path('add/', UserCommunications.as_view()),
    path('graph/', GraphCommunication.as_view()),
]
