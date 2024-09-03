from django.http import HttpResponse
from rest_framework.generics import RetrieveAPIView  # type: ignore
from rest_framework import viewsets  # type: ignore

from .models import GalleryImage
from .serializers import ImageSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = ImageSerializer


class GalleryPreview(RetrieveAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = ImageSerializer

    def get(self, request, *args, **kwargs):
        obj = super().get_object()
        return HttpResponse(obj.image, content_type="image/jpg")
