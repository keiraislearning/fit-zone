from django.urls import path
from main.views import create_produk, show_main, show_produk, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-produk/', create_produk, name='create_produk'),
    path('fit/<str:id>/', show_produk, name='show_produk'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:produk_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:produk_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
