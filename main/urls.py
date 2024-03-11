from django.urls import path
from . import views 
from .views import SchoolListAPIView
from .views import SummaryListAPIView
from .views import ClassListAPIView

urlpatterns = [
    
    path('api/schools/', SchoolListAPIView.as_view(), name='school-list'),
    path('api/class/', ClassListAPIView.as_view(), name='class-list'),
    path('api/summary/', views.SummaryListAPIView.as_view(), name='summary-list'),
     
      
]

