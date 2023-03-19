import csv
import datetime

from django.db.models import QuerySet
from django.db.models.options import Options
from django.http import HttpResponse, HttpRequest


class ExportTlgUsersAsCSVMixin:
    """
    Экспорт TLG пользователей в таблицу формата CSV.
    """
    def export_csv_for_dyatel_project(self, request: HttpRequest, queryset: QuerySet):
        """
        Метод, который будет экспортировать данные о пользователях в таблицу для проекта Dyatel.
        Поля таблицы Client Name, Client Contact, Amount, Payment Date.
        """
        meta: Options = self.model._meta
        # Подготовим объект, в который будут выводится данные - это будет HttpResponse
        response = HttpResponse(content_type='text/csv')  # В объект сразу запишем заголовок content_type
        # Дадим название файлу
        response['Content-Disposition'] = f'attachment; filename={meta.verbose_name_plural}_for_Dyatel_proj--export.csv'

        # Запишем результат в ответ
        csv_writer = csv.writer(response)  # обычно в writer() указываем файл для записи, у нас это response
        csv_writer.writerow(['Client Name', 'Client Contact', 'Amount', 'Payment Date'])  # Записываем заголовки
        for i_obj in queryset:
            # Записываем значение для 'Client Name'
            if i_obj.first_name:
                client_name = getattr(i_obj, 'first_name')
            elif i_obj.username:
                client_name = getattr(i_obj, 'username')
            else:
                client_name = 'Не указано'
            csv_writer.writerow([client_name, getattr(i_obj, 'tlg_id'), 0.00, datetime.date.today()])
        # Отдаём файл. Django всё обработает, а браузер скачает, так как указан attachment
        return response

    export_csv_for_dyatel_project.short_description = 'Экспорт в таблицу для Dyatel project'
