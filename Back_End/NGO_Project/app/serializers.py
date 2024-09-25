from rest_framework import serializers
from .models import *


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegistrationModel
        fields = "__all__"
        
        
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model= AdminModel
        fields= "__all__"
    