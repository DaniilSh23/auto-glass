from django.contrib import admin

from admin_panel.admin_mixins import ExportTlgUsersAsCSVMixin
from admin_panel.models import GlassReplace, ChipsAndCracksRepair, GlassTinting, BuyGlass, \
    ChipsAndCracksPhotos, GlassTintingPhotos, KeyValueStorage, TlgUser


class GlassReplaceAdmin(admin.ModelAdmin):
    list_display = [
        'car_brand',
        'issue_year',
        'convenient_datetime',
        'recording_datetime'
    ]
    list_display_links = [
        'car_brand',
        'issue_year',
        'convenient_datetime',
        'recording_datetime'
    ]


class ChipsAndCracksRepairAdmin(admin.ModelAdmin):
    list_display = [
        'car_brand',
        'convenient_datetime',
        'recording_datetime'
    ]
    list_display_links = [
        'car_brand',
        'convenient_datetime',
        'recording_datetime'
    ]


class GlassTintingAdmin(admin.ModelAdmin):
    list_display = [
        'car_brand',
        'convenient_datetime',
        'recording_datetime',
        'old_film'
    ]
    list_display_links = [
        'car_brand',
        'convenient_datetime',
        'recording_datetime',
        'old_film'
    ]


class BuyGlassAdmin(admin.ModelAdmin):
    list_display = [
        'car_brand',
        'issue_year',
        'convenient_datetime',
        'recording_datetime',
        'need_install'
    ]
    list_display_links = [
        'car_brand',
        'issue_year',
        'convenient_datetime',
        'recording_datetime',
        'need_install'
    ]


class ChipsAndCracksPhotosAdmin(admin.ModelAdmin):
    list_display = ['bid', 'photo', 'upload_datetime']
    list_display_links = ['bid', 'photo', 'upload_datetime']


class GlassTintingPhotosAdmin(admin.ModelAdmin):
    list_display = ['bid', 'photo', 'upload_datetime']
    list_display_links = ['bid', 'photo', 'upload_datetime']


class KeyValueStorageAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    list_display_links = ['key', 'value']


@admin.register(TlgUser)
class TlgUserAdmin(admin.ModelAdmin, ExportTlgUsersAsCSVMixin):
    """
    Регистрация модели TlgUser в админке.
    """
    actions = [
        'export_csv_for_dyatel_project',
    ]
    list_display = (
        "tlg_id",
        "first_name",
        "username",
    )
    list_display_links = (
        "tlg_id",
        "first_name",
        "username",
    )
    search_fields = "tlg_id", "first_name", "username"
    search_help_text = "Поиск по TG ID, TG имени, TG username"
    ordering = ['-id']
    fieldsets = [
        ('Основная информация', {
            "fields": ("tlg_id", "username", "first_name", "last_name"),
            "classes": ("wide", "extrapretty"),
            "description": "Основные данные о пользвателе Telegram.",
        }),
        ('Дополнительная информация', {
            'fields': ('is_premium', 'language_code'),
            'classes': ('wide', 'collapse'),
            'description': 'Дополнительная информация о пользователе Telegram, '
                           'такая как: верификация, мошенничество и т.д.',
        })
    ]


admin.site.register(KeyValueStorage, KeyValueStorageAdmin)
admin.site.register(GlassTintingPhotos, GlassTintingPhotosAdmin)
admin.site.register(ChipsAndCracksPhotos, ChipsAndCracksPhotosAdmin)
admin.site.register(BuyGlass, BuyGlassAdmin)
admin.site.register(GlassTinting, GlassTintingAdmin)
admin.site.register(ChipsAndCracksRepair, ChipsAndCracksRepairAdmin)
admin.site.register(GlassReplace, GlassReplaceAdmin)
