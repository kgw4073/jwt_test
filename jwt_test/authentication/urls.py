from django.urls import path

from .views import (
    RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView, ListView, PostView
)

app_name = 'authentication'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('post/', PostView.as_view()),

]