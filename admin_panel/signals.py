import os

from django.conf import settings
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from admin_panel.models import ChipsAndCracksPhotos, GlassTintingPhotos


@receiver(pre_delete, sender=ChipsAndCracksPhotos)
def delete_chips_photo(sender, instance, **kwargs):
    """
    Функция, которая получает сигнал при удалении объекта модели ChipsAndCracksPhotos и удаляет файл с фоткой.
    """
    if instance.photo:
        file_path = os.path.join(settings.MEDIA_ROOT, instance.tlg_session_file.name)
        if os.path.exists(file_path):
            os.remove(file_path)


@receiver(pre_delete, sender=GlassTintingPhotos)
def delete_glass_tinting_photo(sender, instance, **kwargs):
    """
    Функция, которая получает сигнал при удалении объекта модели GlassTintingPhotos и удаляет файл с фоткой.
    """
    if instance.photo:
        file_path = os.path.join(settings.MEDIA_ROOT, instance.tlg_session_file.name)
        if os.path.exists(file_path):
            os.remove(file_path)
