# Generated by Django 4.1.5 on 2023-03-18 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0005_tlguser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tlguser',
            name='is_fake',
        ),
        migrations.RemoveField(
            model_name='tlguser',
            name='is_scam',
        ),
        migrations.RemoveField(
            model_name='tlguser',
            name='is_verified',
        ),
    ]