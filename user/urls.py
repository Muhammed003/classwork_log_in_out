from django.urls import path
from .views import LogoutAPIView, LoginAPIView


urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),

]