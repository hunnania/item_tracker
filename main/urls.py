from django.urls import path
from main.views import show_json, show_json_by_id, show_main, input_item, show_xml, show_xml_by_id, register, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('input-item', input_item, name='input_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('main/increment/<int:product_id>/', show_main, {'action': 'increment'}, name='increment_amount'),
    path('main/decrement/<int:product_id>/', show_main, {'action': 'decrement'}, name='decrement_amount'),
    path('main/decrement/<int:product_id>/', show_main, {'action': 'decrement'}, name='decrement_amount'),
    path('main/delete/<int:product_id>/', show_main, {'action': 'delete'}, name='delete_item'),
]