from django.urls import path
from main.views import add_product_ajax, decrement, delete, get_product_json, increment, show_json, show_json_by_id, show_main, input_item, show_xml, show_xml_by_id, register, login_user, logout_user

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
    path('increment/<int:id>/', increment, name='increment_amount'),
    path('decrement/<int:id>/', decrement, name='decrement_amount'),
    path('delete/<int:id>/', delete, name='delete_item'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
]