# Generated by Django 4.1.5 on 2023-02-15 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tlg_id', models.CharField(max_length=20, verbose_name='TG ID')),
                ('tlg_username', models.CharField(blank=True, max_length=100, null=True, verbose_name='TG username')),
                ('tlg_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='TG имя')),
                ('tlg_lastname', models.CharField(blank=True, max_length=100, null=True, verbose_name='TG фамилия')),
            ],
            options={
                'verbose_name': 'Пользователь бота',
                'verbose_name_plural': 'Пользователи бота',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='BuyGlass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=100, verbose_name='Марка авто')),
                ('car_body_type', models.CharField(choices=[('sd', 'судан'), ('htch', 'хэтчбэк'), ('un', 'универсал')], default='sd', max_length=4, verbose_name='Тип кузова')),
                ('issue_year', models.CharField(max_length=10, verbose_name='Год выпуска')),
                ('glass_type', models.CharField(choices=[('front', 'лобовое'), ('side', 'боковое'), ('rear', 'заднее')], max_length=5, verbose_name='Стекло')),
                ('full_glass_heating', models.BooleanField(verbose_name='полный обогрев стекла')),
                ('wiper_heating', models.BooleanField(verbose_name='обогрев зоны дворников')),
                ('rain_sensor', models.BooleanField(verbose_name='датчик долждя')),
                ('camera_assistant', models.BooleanField(verbose_name='камера-ассистент')),
                ('vin_code_windows', models.BooleanField(verbose_name='окошко под VIN')),
                ('projection', models.BooleanField(verbose_name='проекция')),
                ('i_dont_know', models.BooleanField(verbose_name='не знаю')),
                ('convenient_datetime', models.DateTimeField(null=True, verbose_name='Удобное время и дата')),
                ('contacts', models.CharField(max_length=250, verbose_name='Контактные данные')),
                ('need_install', models.BooleanField(verbose_name='Требуется установка')),
                ('recording_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заявки')),
            ],
            options={
                'verbose_name': 'Заявка на покупку стекла',
                'verbose_name_plural': 'Заявки на покупку стекол',
                'ordering': ['-recording_datetime'],
            },
        ),
        migrations.CreateModel(
            name='ChipsAndCracksRepair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=100, verbose_name='Марка авто')),
                ('glass_type', models.CharField(choices=[('front', 'лобовое'), ('side', 'боковое'), ('rear', 'заднее')], max_length=5, verbose_name='Стекло')),
                ('convenient_datetime', models.DateTimeField(null=True, verbose_name='Удобное время и дата')),
                ('contacts', models.CharField(max_length=250, verbose_name='Контактные данные')),
                ('recording_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заявки')),
            ],
            options={
                'verbose_name': 'Заявка на ремонт сколов и трещин',
                'verbose_name_plural': 'Заявки на ремонт сколов и трещин',
                'ordering': ['-recording_datetime'],
            },
        ),
        migrations.CreateModel(
            name='GlassReplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=100, verbose_name='Марка авто')),
                ('car_body_type', models.CharField(choices=[('sd', 'судан'), ('htch', 'хэтчбэк'), ('un', 'универсал')], default='sd', max_length=4, verbose_name='Тип кузова')),
                ('issue_year', models.CharField(max_length=10, verbose_name='Год выпуска')),
                ('glass_type', models.CharField(choices=[('front', 'лобовое'), ('side', 'боковое'), ('rear', 'заднее')], max_length=5, verbose_name='Стекло')),
                ('full_glass_heating', models.BooleanField(verbose_name='полный обогрев стекла')),
                ('wiper_heating', models.BooleanField(verbose_name='обогрев зоны дворников')),
                ('rain_sensor', models.BooleanField(verbose_name='датчик долждя')),
                ('camera_assistant', models.BooleanField(verbose_name='камера-ассистент')),
                ('vin_code_windows', models.BooleanField(verbose_name='окошко под VIN')),
                ('projection', models.BooleanField(verbose_name='проекция')),
                ('i_dont_know', models.BooleanField(verbose_name='не знаю')),
                ('convenient_datetime', models.DateTimeField(null=True, verbose_name='Удобное время и дата')),
                ('contacts', models.CharField(max_length=250, verbose_name='Контактные данные')),
                ('recording_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заявки')),
            ],
            options={
                'verbose_name': 'Заявка на замену стекла',
                'verbose_name_plural': 'Заявки на замену стекол',
                'ordering': ['-recording_datetime'],
            },
        ),
        migrations.CreateModel(
            name='GlassTinting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=100, verbose_name='Марка авто')),
                ('glass_type', models.CharField(choices=[('front', 'лобовое'), ('side', 'боковое'), ('rear', 'заднее')], max_length=5, verbose_name='Стекло')),
                ('convenient_datetime', models.DateTimeField(null=True, verbose_name='Удобное время и дата')),
                ('contacts', models.CharField(max_length=250, verbose_name='Контактные данные')),
                ('old_film', models.BooleanField(verbose_name='Старая плёнка')),
                ('recording_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заявки')),
            ],
            options={
                'verbose_name': 'Заявка на тонировку',
                'verbose_name_plural': 'Заявки на тонировку',
                'ordering': ['-recording_datetime'],
            },
        ),
        migrations.CreateModel(
            name='GlassTintingPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время загрузки')),
                ('photo', models.FileField(upload_to='glass_tinting_photo/')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.chipsandcracksrepair', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Фото для заявки на тонировку',
                'verbose_name_plural': 'Фото для заявок на тонировку',
                'ordering': ['-upload_datetime'],
            },
        ),
        migrations.CreateModel(
            name='ChipsAndCracksPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время загрузки')),
                ('photo', models.FileField(upload_to='chips_and_cracks_photo/')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.chipsandcracksrepair', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Фото для заявки на ремонт сколов и трещин',
                'verbose_name_plural': 'Фото для заявок на ремонт сколов и трещин',
                'ordering': ['-upload_datetime'],
            },
        ),
    ]
