from django.urls import path

from .views import SellingPostView
app_name = 'authentication'
urlpatterns = [
    path('selling/', SellingPostView.as_view()),

]