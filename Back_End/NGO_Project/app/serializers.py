from rest_framework import serializers
from .models import SuperAdminModel


class SuperAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=SuperAdminModel
        fields =["id","name","email","contact","password","confirm_password"]
