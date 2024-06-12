from django.urls import path
from .views import ProgressListCreateView, ProgressDetailView

urlpatterns = [
    path('', ProgressListCreateView.as_view(), name='progress-list-create'),
    path('<int:pk>/', ProgressDetailView.as_view(), name='progress-detail')
]
