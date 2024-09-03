from celery import shared_task, uuid  # type: ignore
from celery import Celery  # type: ignore
from django.conf import settings
import requests
from PIL import Image

from .models import GalleryImage


app = Celery()


EXTERNAL_API_URL = settings.EXTERNAL_API_URL


@shared_task(bind=True)
def download_external_image(self, image_obj_id: int) -> None:
    file_name = uuid()
    ext = ".jpeg"

    with requests.get(EXTERNAL_API_URL, stream=True) as r:
        r.raise_for_status()
        with open(f'gallery_images/{file_name}{ext}', 'wb') as f:
            for block in r:
                f.write(block)

    im = Image.open(f'gallery_images/{file_name}{ext}')
    im.thumbnail((200, 200), Image.Resampling.LANCZOS)
    im.save(f'gallery_images/{file_name}_resized{ext}', 'JPEG')

    GalleryImage.objects.filter(id=image_obj_id).update(image=f'gallery_images/{file_name}_resized{ext}')
