from django.urls import path
from .views import *

app_name = 'personal'

urlpatterns = [
    path('portfolio/<int:pk>/', PortfolioDetail.as_view()),
    path('blog/<int:pk>/', BlogDetail.as_view())
]
