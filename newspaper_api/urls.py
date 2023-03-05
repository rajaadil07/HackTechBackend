from django.urls import path
from .views import NewsPaperAPIView

urlpatterns = [
    path("newspaper/",NewsPaperAPIView.as_view(),name='newspaper'),
]