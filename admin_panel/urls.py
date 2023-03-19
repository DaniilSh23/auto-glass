from django.urls import path
from admin_panel.views import test_view, glass_replace_view, send_form, chips_repair_view, \
    glass_tinting_view, buy_glass_view, TlgUserView

app_name = 'auto_glass'

urlpatterns = [
    path('test/', test_view, name='test'),
    path('', send_form, name='send_form'),
    path('glass_rplc/', glass_replace_view, name='glass_rplc'),
    path('chips_repair/', chips_repair_view, name='chips_repair'),
    path('tinting/', glass_tinting_view, name='tinting'),
    path('buy_glass/', buy_glass_view, name='buy_glass'),
    path('users_data/', TlgUserView.as_view(), name='users_data'),
]
