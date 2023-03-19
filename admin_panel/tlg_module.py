import requests
from admin_panel.models import KeyValueStorage
from loguru import logger


def send_tlg_notifications(text):
    """
    Отправка уведомлений в телеграм.
    """
    bot_token = KeyValueStorage.objects.get(key='bot_token').value
    recipients_lst = KeyValueStorage.objects.filter(key='tlg_admin_id')
    counter = 0
    for i_rec in recipients_lst:
        send_rslt = requests.post(
            url=f'https://api.telegram.org/bot{bot_token}/sendMessage',
            data={
                'chat_id': i_rec.value,
                'text': 'Новая заявка !\n\n'
                        f'{text}'
            }
        )
        if send_rslt.status_code != 400:
            counter += 1
            logger.success(f'Успешная отправка уведомления о заявке в телеграм ID получателя {i_rec.value}')
        else:
            logger.warning(f'НЕ УДАЛАСЬ отправка уведомления о заявке в телеграм ID получателя {i_rec.value}')
    else:
        logger.info(f'Рассылка уведомлений в телеграм завершена. '
                    f'Отправлено {counter} из {len(recipients_lst)} уведомлений')
