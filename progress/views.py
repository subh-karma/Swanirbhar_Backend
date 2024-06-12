from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Progress
from .serializers import ProgressSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ProgressListCreateView(generics.ListCreateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class ProgressDetailView(generics.RetrieveUpdateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
