import pytest
from django.urls import reverse
from rest_framework import status  # type: ignore
from rest_framework.test import APIClient  # type: ignore

from images.models import GalleryImage


@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_gallery_viewset_list(api_client):
    image_obj1 = GalleryImage.objects.create(image="image1_resized.jpeg")
    image_obj2 = GalleryImage.objects.create(image="image2_resized.jpeg")

    url = reverse('galleryimage-list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 2
    assert response.data['results'][0]['id'] == image_obj1.id
    assert response.data['results'][1]['id'] == image_obj2.id

@pytest.mark.django_db
def test_gallery_viewset_retrieve(api_client):
    image_obj = GalleryImage.objects.create(image="image_resized.jpeg")

    url = reverse('galleryimage-detail', args=[image_obj.id])
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == image_obj.id


@pytest.mark.django_db
def test_gallery_preview(api_client):
    image_obj = GalleryImage.objects.create(image="gallery_images/sample.jpeg")

    url = reverse('gallery-preview', args=[image_obj.id])
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response['Content-Type'] == 'image/jpg'
    assert response.content == image_obj.image.read()
