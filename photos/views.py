from django.http import HttpResponse
from rest_framework import viewsets, parsers
from .models import Photo
from .serializers import PhotoSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class PhotoViewset(viewsets.ModelViewSet):
 
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']

