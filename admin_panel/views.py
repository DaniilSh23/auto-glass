from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from loguru import logger
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from admin_panel.models import GlassReplace, ChipsAndCracksRepair, ChipsAndCracksPhotos, GlassTinting, \
    GlassTintingPhotos, BuyGlass, TlgUser
from admin_panel.serializers import TlgUserSerializer
from admin_panel.tlg_module import send_tlg_notifications
from admin_panel.whatsapp_module import send_notification_to_whatsapp
from forms import GlassReplaceForm, ChipsAndCracksRepairForm, PhotoChipsAndCracksRepairForm, GlassTintingForm, \
    PhotoGlassTintingForm, BuyGlassForm


def test_view(request):
    if request.method == 'GET':
        glass_replace_form = GlassReplaceForm()
        chips_repair_form = ChipsAndCracksRepairForm()
        context = {
            'glass_replace_form': glass_replace_form,
            'chips_repair_form': chips_repair_form,
        }
        # return render(request, 'forms.html', context=context)
        # return render(request, 'success_page.html', context=context)
        # return render(request, 'test.html', context=context)


def send_form(request):
    """
    Вьюшка для отправки формы.
    """
    if request.method == 'GET':
        glass_replace_form = GlassReplaceForm()
        chips_repair_form = ChipsAndCracksRepairForm()
        photo_chips_repair_form = PhotoChipsAndCracksRepairForm()
        glass_tinting_form = GlassTintingForm()
        photo_glass_tinting_form = PhotoGlassTintingForm()
        buy_glass_form = BuyGlassForm()
        context = {
            'glass_replace_form': glass_replace_form,
            'chips_repair_form': chips_repair_form,
            'photo_chips_repair_form': photo_chips_repair_form,
            'glass_tinting_form': glass_tinting_form,
            'photo_glass_tinting_form': photo_glass_tinting_form,
            'buy_glass_form': buy_glass_form,
        }
        return render(request, 'forms.html', context=context)


@csrf_exempt
def glass_replace_view(request):
    """
    POST запрос. Принимаем заявку на замену стекла.
    """
    form = GlassReplaceForm(request.POST)
    if form.is_valid():
        instance = GlassReplace(**form.cleaned_data)
        instance.save()
        context = {
            'car_brand': form.cleaned_data.get("car_brand"),
            'convenient_datetime': form.cleaned_data.get("convenient_datetime"),
            'contacts': form.cleaned_data.get("contacts"),
            'service_type': 'замена стекла'
        }
        # Отправка уведомления в телеграм
        send_tlg_notifications(
            text='Услуга: замена стекла\n'
                 f'Марка авто: {form.cleaned_data.get("car_brand")}\n'
                 f'Удобное время и дата: {form.cleaned_data.get("convenient_datetime")}\n'
                 f'Контакты: {form.cleaned_data.get("contacts")}\n'
        )
        # Отправка уведомления в WhatsApp
        send_notification_to_whatsapp(
            car_brand=form.cleaned_data.get("car_brand"),
            contacts=form.cleaned_data.get("contacts"),
            convenient_datetime=form.cleaned_data.get("convenient_datetime"),
            service_type='замена стекла',
        )
        return render(request, 'success_page.html', context=context)


@csrf_exempt
def chips_repair_view(request):
    """
    POST запрос. Принимаем заявку на ремонт сколов и трещин
    """
    form = ChipsAndCracksRepairForm(request.POST)
    photo_form = PhotoChipsAndCracksRepairForm(request.POST, request.FILES)
    if form.is_valid() and photo_form.is_valid():
        instance = ChipsAndCracksRepair(**form.cleaned_data)
        instance.save()
        files_lst = request.FILES.getlist('photo')
        for i_file in files_lst:
            file_obj = ChipsAndCracksPhotos(bid=instance, photo=i_file)
            file_obj.save()
        context = {
            'car_brand': form.cleaned_data.get("car_brand"),
            'convenient_datetime': form.cleaned_data.get("convenient_datetime"),
            'contacts': form.cleaned_data.get("contacts"),
            'service_type': 'ремонт сколов и трещин'
        }
        # Отправка уведомления в телеграм
        send_tlg_notifications(
            text='Услуга: ремонт сколов и трещин\n'
                 f'Марка авто: {form.cleaned_data.get("car_brand")}\n'
                 f'Удобное время и дата: {form.cleaned_data.get("convenient_datetime")}\n'
                 f'Контакты: {form.cleaned_data.get("contacts")}\n'
        )
        # Отправка уведомления в WhatsApp
        send_notification_to_whatsapp(
            car_brand=form.cleaned_data.get("car_brand"),
            contacts=form.cleaned_data.get("contacts"),
            convenient_datetime=form.cleaned_data.get("convenient_datetime"),
            service_type='ремонт сколов и трещин',
        )
        return render(request, 'success_page.html', context=context)


@csrf_exempt
def glass_tinting_view(request):
    """
    POST запрос. Принимаем заявку на тонировку
    """
    form = GlassTintingForm(request.POST)
    photo_form = PhotoGlassTintingForm(request.POST, request.FILES)
    if form.is_valid() and photo_form.is_valid():
        instance = GlassTinting(**form.cleaned_data)
        instance.save()
        files_lst = request.FILES.getlist('photo')
        for i_file in files_lst:
            file_obj = GlassTintingPhotos(bid=instance, photo=i_file)
            file_obj.save()
        context = {
            'car_brand': form.cleaned_data.get("car_brand"),
            'convenient_datetime': form.cleaned_data.get("convenient_datetime"),
            'contacts': form.cleaned_data.get("contacts"),
            'service_type': 'тонировка'
        }
        # Отправка уведомления в телеграм
        send_tlg_notifications(
            text='Услуга: тонировка\n'
                 f'Марка авто: {form.cleaned_data.get("car_brand")}\n'
                 f'Удобное время и дата: {form.cleaned_data.get("convenient_datetime")}\n'
                 f'Контакты: {form.cleaned_data.get("contacts")}\n'
        )
        # Отправка уведомления в WhatsApp
        send_notification_to_whatsapp(
            car_brand=form.cleaned_data.get("car_brand"),
            contacts=form.cleaned_data.get("contacts"),
            convenient_datetime=form.cleaned_data.get("convenient_datetime"),
            service_type='тонировка',
        )
        return render(request, 'success_page.html', context=context)


@csrf_exempt
def buy_glass_view(request):
    """
    POST запрос. Принимаем заявку на покупку стекла.
    """
    form = BuyGlassForm(request.POST)
    if form.is_valid():
        instance = BuyGlass(**form.cleaned_data)
        instance.save()
        context = {
            'car_brand': form.cleaned_data.get("car_brand"),
            'convenient_datetime': form.cleaned_data.get("convenient_datetime"),
            'contacts': form.cleaned_data.get("contacts"),
            'service_type': 'покупка стекла'
        }
        # Отправка уведомления в телеграм
        send_tlg_notifications(
            text='Услуга: покупка стекла\n'
                 f'Марка авто: {form.cleaned_data.get("car_brand")}\n'
                 f'Удобное время и дата: {form.cleaned_data.get("convenient_datetime")}\n'
                 f'Контакты: {form.cleaned_data.get("contacts")}\n'
        )
        # Отправка уведомления в WhatsApp
        send_notification_to_whatsapp(
            car_brand=form.cleaned_data.get("car_brand"),
            contacts=form.cleaned_data.get("contacts"),
            convenient_datetime=form.cleaned_data.get("convenient_datetime"),
            service_type='покупка стекла',
        )
        return render(request, 'success_page.html', context=context)


class TlgUserView(APIView):
    """
    Вьюшка для обработки запросов, связанных с моделью TlgUser.
    """
    def post(self, request, format=None):
        """
        Обработка POST запроса.
        """
        logger.info(f'Получен запрос от бота на запись пользователя.')
        serializer = TlgUserSerializer(data=request.data)
        if serializer.is_valid():
            tlg_user_obj = TlgUser.objects.update_or_create(
                tlg_id=serializer.data.get('tlg_id'),
                defaults=serializer.data
            )
            logger.success(f'Пользователь бота c TG_ID == {serializer.data.get("tlg_id")} '
                           f'был {"создан" if tlg_user_obj[1] else "обновлён"}.')
            result_object = TlgUserSerializer(tlg_user_obj[0], many=False).data
            return Response(result_object, status.HTTP_200_OK)
        else:
            logger.warning(f'Данные от бота на запись пользователя не прошли валидацию.')
            return Response({'result': 'Переданные данные не прошли валидацию'}, status.HTTP_400_BAD_REQUEST)
