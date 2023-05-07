from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(label = "Enter Project Id")
    project_name = serializers.CharField(label = "Enter Client Name")
    #created_at = models.DateTimeField(blank=True)
    created_by = serializers.CharField(label = "Enter Created By")
    
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client1
        fields = "__all__"