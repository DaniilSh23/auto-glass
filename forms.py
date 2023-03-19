from django import forms


class GlassReplaceForm(forms.Form):
    """
    Форма для заявки по замене стекла
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
    car_brand = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required"
    }))
    car_body_type = forms.ChoiceField(choices=CAR_BODY_LST, widget=forms.Select(attrs={
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required",
    }))
    issue_year = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required"
    }))
    glass_type = forms.ChoiceField(choices=GLASS_TYPE_LST, widget=forms.Select(attrs={
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required",
    }))
    '''Комплектация стекла(начало)'''
    full_glass_heating = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "ch-1-1",
    }))
    wiper_heating = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "ch-1-2",
    }))
    rain_sensor = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "ch-1-3",
    }))
    camera_assistant = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "ch-1-4",
    }))
    vin_code_windows = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "ch-1-5",
    }))
    projection = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "ch-1-6",
    }))
    i_dont_know = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "ch-1-7",
    }))
    '''Комплектация стекла(конец)'''
    convenient_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        "type": "datetime-local",
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required",
    }))
    contacts = forms.CharField(widget=forms.Textarea(attrs={
        "class": "wq-form__input wq-form__item",
        "placeholder": "имя и номер телефона",
        "required": "required",
        "rows": "",
        "cols": ""
    }))


class ChipsAndCracksRepairForm(forms.Form):
    """
    Форма для заявки по ремонту сколов и трещин.
    """
    GLASS_TYPE_LST = [
        ('front', 'Лобовое'),
        ('side', 'Боковое'),
        ('rear', 'Заднее'),
    ]
    car_brand = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required"
    }))
    glass_type = forms.ChoiceField(choices=GLASS_TYPE_LST, widget=forms.Select(attrs={
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required",
    }))
    convenient_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        "type": "datetime-local",
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required",
    }))
    contacts = forms.CharField(widget=forms.Textarea(attrs={
        "class": "wq-form__input wq-form__item",
        "placeholder": "имя и номер телефона",
        "required": "required",
        "rows": "",
        "cols": ""
    }))


class PhotoChipsAndCracksRepairForm(forms.Form):
    """
    Форма для фоток к заявками на ремонт сколов и трещин.
    """
    photo = forms.FileField(widget=forms.ClearableFileInput(attrs={
        "multiple": True,
        # "type": "file",
        # "style": "display: none",
        "id": "file-2"
    }))


class GlassTintingForm(forms.Form):
    """
    Форма для заявок на тонировку.
    """
    GLASS_TYPE_LST = [
        ('front', 'Лобовое'),
        ('side', 'Боковое'),
        ('rear', 'Заднее'),
    ]
    OLD_FILM_CHOICE = [
        (True, 'Да'),
        (False, 'Нет'),
    ]
    car_brand = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required"
    }))
    glass_type = forms.ChoiceField(choices=GLASS_TYPE_LST, widget=forms.Select(attrs={
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required",
    }))
    convenient_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        "type": "datetime-local",
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required",
    }))
    contacts = forms.CharField(widget=forms.Textarea(attrs={
        "class": "wq-form__input wq-form__item",
        "placeholder": "имя и номер телефона",
        "required": "required",
        "rows": "",
        "cols": ""
    }))
    old_film = forms.ChoiceField(choices=OLD_FILM_CHOICE, widget=forms.Select(attrs={
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required",
    }))


class PhotoGlassTintingForm(forms.Form):
    """
    Форма для фоток к заявкам на тонировку.
    """
    photo = forms.FileField(widget=forms.ClearableFileInput(attrs={
        "multiple": True,
        # "type": "file",
        # "style": "display: none",
        "id": "file-1"
    }))


class BuyGlassForm(forms.Form):
    """
    Форма для заявки на покупку стекла
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
    car_brand = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required"
    }))
    car_body_type = forms.ChoiceField(choices=CAR_BODY_LST, widget=forms.Select(attrs={
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required",
    }))
    issue_year = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required"
    }))
    glass_type = forms.ChoiceField(choices=GLASS_TYPE_LST, widget=forms.Select(attrs={
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required",
    }))
    '''Комплектация стекла(начало)'''
    full_glass_heating = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "ch-2-1",
    }))
    wiper_heating = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "ch-2-2",
    }))
    rain_sensor = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "ch-2-3",
    }))
    camera_assistant = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "ch-2-4",
    }))
    vin_code_windows = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "ch-2-5",
    }))
    projection = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "ch-2-6",
    }))
    i_dont_know = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "type": "checkbox",
        "id": "ch-2-7",
    }))
    '''Комплектация стекла(конец)'''
    convenient_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        "type": "datetime-local",
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required",
    }))
    contacts = forms.CharField(widget=forms.Textarea(attrs={
        "class": "wq-form__input wq-form__item",
        "placeholder": "имя и номер телефона",
        "required": "required",
        "rows": "",
        "cols": ""
    }))
    NEED_INSTALL_CHOICE = [
        (True, 'Да'),
        (False, 'Нет'),
    ]
    need_install = forms.ChoiceField(choices=NEED_INSTALL_CHOICE, widget=forms.Select(attrs={
        "class": "wq-form__input wq-form__item",
        "placeholder": "Ответ",
        "required": "required",
    }))