from django.db import models


class GlassReplace(models.Model):
    """
    Модель заявок по замене стекла.
    """
    CAR_BODY_LST = [
        ('sd', 'Седан'),
        ('htch', 'Хэтчбэк'),
        ('un', 'Универсал'),
    ]
    GLASS_TYPE_LST = [
        ('front', 'Лобовое'),
        ('side', 'Боковое'),
        ('rear', 'Заднее'),
    ]
    car_brand = models.CharField(verbose_name='Марка авто', max_length=100)
    car_body_type = models.CharField(verbose_name='Тип кузова', choices=CAR_BODY_LST, max_length=4, default='sd')
    issue_year = models.CharField(verbose_name='Год выпуска', max_length=10)
    glass_type = models.CharField(verbose_name='Стекло', choices=GLASS_TYPE_LST, max_length=5)
    '''Комплектация стекла(начало)'''
    full_glass_heating = models.BooleanField(verbose_name='полный обогрев стекла', default=False)
    wiper_heating = models.BooleanField(verbose_name='обогрев зоны дворников', default=False)
    rain_sensor = models.BooleanField(verbose_name='датчик долждя', default=False)
    camera_assistant = models.BooleanField(verbose_name='камера-ассистент', default=False)
    vin_code_windows = models.BooleanField(verbose_name='окошко под VIN', default=False)
    projection = models.BooleanField(verbose_name='проекция', default=False)
    i_dont_know = models.BooleanField(verbose_name='не знаю', default=False)
    '''Комплектация стекла(конец)'''
    convenient_datetime = models.DateTimeField(verbose_name='Удобное время и дата', null=True)
    contacts = models.CharField(verbose_name='Контактные данные', max_length=250)
    recording_datetime = models.DateTimeField(verbose_name='Дата и время заявки', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на замену стекла'
        verbose_name_plural = 'Заявки на замену стекол'
        ordering = ['-recording_datetime']

    def __str__(self):
        return f'Заявка на замену стекла: {self.contacts}'


class ChipsAndCracksRepair(models.Model):
    """
    Модель заявок ремонта сколов и трещин.
    """
    GLASS_TYPE_LST = [
        ('front', 'Лобовое'),
        ('side', 'Боковое'),
        ('rear', 'Заднее'),
    ]
    car_brand = models.CharField(verbose_name='Марка авто', max_length=100)
    glass_type = models.CharField(verbose_name='Стекло', choices=GLASS_TYPE_LST, max_length=5)
    convenient_datetime = models.DateTimeField(verbose_name='Удобное время и дата', null=True)
    contacts = models.CharField(verbose_name='Контактные данные', max_length=250)
    recording_datetime = models.DateTimeField(verbose_name='Дата и время заявки', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на ремонт сколов и трещин'
        verbose_name_plural = 'Заявки на ремонт сколов и трещин'
        ordering = ['-recording_datetime']

    def __str__(self):
        return f'Заявка на ремонт сколов и трещин: {self.contacts}'


class ChipsAndCracksPhotos(models.Model):
    """
    Фотки для сколов и трещин.
    """
    bid = models.ForeignKey(verbose_name='Заявка', to=ChipsAndCracksRepair, on_delete=models.CASCADE)
    upload_datetime = models.DateTimeField(verbose_name='Дата и время загрузки', auto_now_add=True)
    photo = models.FileField(upload_to='chips_and_cracks_photo/')

    class Meta:
        verbose_name = 'Фото для заявки на ремонт сколов и трещин'
        verbose_name_plural = 'Фото для заявок на ремонт сколов и трещин'
        ordering = ['-upload_datetime']


class GlassTinting(models.Model):
    """
    Модель заявок на тонировку.
    """
    GLASS_TYPE_LST = [
        ('front', 'Лобовое'),
        ('side', 'Боковое'),
        ('rear', 'Заднее'),
    ]
    car_brand = models.CharField(verbose_name='Марка авто', max_length=100)
    glass_type = models.CharField(verbose_name='Стекло', choices=GLASS_TYPE_LST, max_length=5)
    convenient_datetime = models.DateTimeField(verbose_name='Удобное время и дата', null=True)
    contacts = models.CharField(verbose_name='Контактные данные', max_length=250)
    old_film = models.BooleanField(verbose_name='Старая плёнка')
    recording_datetime = models.DateTimeField(verbose_name='Дата и время заявки', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на тонировку'
        verbose_name_plural = 'Заявки на тонировку'
        ordering = ['-recording_datetime']

    def __str__(self):
        return f'Заявка на тонировку: {self.contacts}'


class GlassTintingPhotos(models.Model):
    """
    Фотки для заявок на тонировку.
    """
    bid = models.ForeignKey(verbose_name='Заявка', to=GlassTinting, on_delete=models.CASCADE)
    upload_datetime = models.DateTimeField(verbose_name='Дата и время загрузки', auto_now_add=True)
    photo = models.FileField(upload_to='glass_tinting_photo/')

    class Meta:
        verbose_name = 'Фото для заявки на тонировку'
        verbose_name_plural = 'Фото для заявок на тонировку'
        ordering = ['-upload_datetime']


class BuyGlass(models.Model):
    """
    Заявки на покупку стёкол.
    """
    CAR_BODY_LST = [
        ('sd', 'Седан'),
        ('htch', 'Хэтчбэк'),
        ('un', 'Универсал'),
    ]
    GLASS_TYPE_LST = [
        ('front', 'Лобовое'),
        ('side', 'Боковое'),
        ('rear', 'Заднее'),
    ]
    car_brand = models.CharField(verbose_name='Марка авто', max_length=100)
    car_body_type = models.CharField(verbose_name='Тип кузова', choices=CAR_BODY_LST, max_length=4, default='sd')
    issue_year = models.CharField(verbose_name='Год выпуска', max_length=10)
    glass_type = models.CharField(verbose_name='Стекло', choices=GLASS_TYPE_LST, max_length=5)
    '''Комплектация стекла(начало)'''
    full_glass_heating = models.BooleanField(verbose_name='полный обогрев стекла')
    wiper_heating = models.BooleanField(verbose_name='обогрев зоны дворников')
    rain_sensor = models.BooleanField(verbose_name='датчик долждя')
    camera_assistant = models.BooleanField(verbose_name='камера-ассистент')
    vin_code_windows = models.BooleanField(verbose_name='окошко под VIN')
    projection = models.BooleanField(verbose_name='проекция')
    i_dont_know = models.BooleanField(verbose_name='не знаю')
    '''Комплектация стекла(конец)'''
    convenient_datetime = models.DateTimeField(verbose_name='Удобное время и дата', null=True)
    contacts = models.CharField(verbose_name='Контактные данные', max_length=250)
    need_install = models.BooleanField(verbose_name='Требуется установка')
    recording_datetime = models.DateTimeField(verbose_name='Дата и время заявки', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на покупку стекла'
        verbose_name_plural = 'Заявки на покупку стекол'
        ordering = ['-recording_datetime']

    def __str__(self):
        return f'Заявка на покупку стекла: {self.contacts}'


class KeyValueStorage(models.Model):
    """
    Модель для хранилища ключ-значение.
    """
    key = models.CharField(verbose_name='ключ', max_length=250)
    value = models.TextField(verbose_name='ключ', max_length=2000)

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
        ordering = ['-id']

    def __str__(self):
        return f'Ключ: {self.key}'


class TlgUser(models.Model):
    """
    Модель пользователя телеграм.
    """
    tlg_id = models.CharField(verbose_name='TG ID', max_length=30)
    is_premium = models.BooleanField(verbose_name='Премиум', default=False)
    first_name = models.CharField(verbose_name='Имя(TG)', max_length=100, blank=True, null=False)
    last_name = models.CharField(verbose_name='Фамилия(TG)', max_length=100, blank=True, null=False)
    username = models.CharField(verbose_name='username(TG)', max_length=100, blank=True, null=False)
    language_code = models.CharField(verbose_name='языковой код(TG)', max_length=20, blank=True, null=False)

    def __str__(self):
        return f'Пользователь с TG ID: {self.tlg_id}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'пользователь TG'
        verbose_name_plural = 'пользователи TG'
