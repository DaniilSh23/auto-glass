from loguru import logger
from whatsapp_api_client_python import API
from whatsapp_api_client_python.response import Response

from admin_panel.models import KeyValueStorage


def send_notification_to_whatsapp(service_type, car_brand, convenient_datetime, contacts):
    """
    Отправка в WhatsApp текстового сообщения - уведомления о новой заявке.
    """
    try:
        id_instance = KeyValueStorage.objects.get(key='green_api_instance_id').value
        api_token_instance = KeyValueStorage.objects.get(key='green_api_token').value
        notification_phone = KeyValueStorage.objects.get(key='whatsapp_notification_phone').value
    except Exception:
        logger.warning(f'Уведомление в WhatsApp не отправлено! В админке не установлены ключи: '
                       f'green_api_instance_id, green_api_token или whatsapp_notification_phone')
        return
    green_api = API.GreenApi(id_instance, api_token_instance)
    send_txt_result: Response = green_api.sending.sendMessage(f'{notification_phone}@c.us',
                                                              'Новый заказ!\n'
                                                              f'Услуга: {service_type}\n'
                                                              f'Марка авто: {car_brand}\n'
                                                              f'Удобное время и дата: {convenient_datetime}\n'
                                                              f'Контакты: {contacts}')
    if send_txt_result.code != 200:
        logger.warning(f'Не удалось отправить уведомление в WhatsApp на номер {notification_phone}!\n'
                       f'Response: {send_txt_result.data}')
    else:
        logger.success(f'Успешная отправка уведомления в WhatsApp на номер {notification_phone}')
