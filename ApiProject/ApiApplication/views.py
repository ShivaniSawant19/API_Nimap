from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.
class ProjectApiView(APIView):
    serializers_class = ProjectSerializer
    def get(self, request):
        allProject = Project.objects.all().values()
        return Response({"Message": "List of Client", "Client and Project List" : allProject})
    
    def post(self, request):
        print('Request data is : ',request.data)
        serializer_obj=ProjectSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Project.objects.create(id=serializer_obj.data.get("id"),
                            project_name=serializer_obj.data.get("project_name"),
                            created_by=serializer_obj.data.get("created_by")
                            )
        
        project = Project.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message" : "New Project added!", "Client and Project": project})             

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client1.objects.all()
    serializers_class = ClientSerializer