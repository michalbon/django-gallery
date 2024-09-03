from rest_framework import serializers  # type: ignore

from .models import GalleryImage
from .tasks import download_external_image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image', 'created_at', 'updated_at']

    def create(self, validated_data):
        instance = super().create(validated_data)
        download_external_image.delay(instance.id)  # async Celery task
        return instance

    def update(self, instance, validated_data):
        download_external_image.delay(instance.id)
        instance.refresh_from_db()
        return super().update(instance, validated_data)
