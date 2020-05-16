import sys
import logging

from PIL import Image
from uuid import uuid4
from io import BytesIO
from uuslug import uuslug,  slugify

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings

log = logging.getLogger(__name__)


class SaveModelSlugMixin:

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(s=self.title, instance=self)
        super().save(*args, **kwargs)


class SaveModelImageMixin:

    def image_stream(self, image, image_size):
        temporary_image = Image.open(image)
        output_io_stream = BytesIO()
        temporary_image = temporary_image.convert("RGB")
        temporary_image.thumbnail(image_size, Image.ANTIALIAS)
        temporary_image.save(output_io_stream, format='JPEG', quality=85)
        output_io_stream.seek(0)
        return output_io_stream

    def save(self, *args, **kwargs):
        if not self.color_slug:
            self.color_slug = slugify(f"{self.title}-{self.element.title}-{uuid4()}")
        try:
            normal_sized_output_io_stream = self.image_stream(self.image, settings.IMAGE_THUMBNAIL_SIZE)
            sm_sized_output_io_stream = self.image_stream(self.image, settings.SM_IMAGE_THUMBNAIL_SIZE)
            self.image = InMemoryUploadedFile(normal_sized_output_io_stream, 'image',
                                              f"{self.image.name.split('.')[0]}.jpg",
                                              'image/jpeg',
                                              sys.getsizeof(normal_sized_output_io_stream), None)
            self.sm_image = InMemoryUploadedFile(sm_sized_output_io_stream, 'image',
                                              f"{self.image.name.split('.')[0]}.jpg",
                                              'image/jpeg',
                                              sys.getsizeof(sm_sized_output_io_stream), None)
        except ValueError:
            log.warning("Удалён image файл с сохранением объекта")
        super().save(*args, **kwargs)