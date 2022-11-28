from core.user.serializers import UserSerializer
from core.user.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

class UserViewSet(viewsets.ModelViewSet):
    http_method_names= ['get']
    serializer_class=UserSerializer
    permission_classes=(IsAuthenticated)
    filter_backends=[filters.OrderingFilter]
    ordering_fields=['updated']
    ordering=['-updated'] 
    
    def get_queryset(self):
        return super().get_queryset()