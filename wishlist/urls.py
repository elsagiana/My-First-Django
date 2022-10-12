from django.urls import path
from wishlist.views import show_wishlist, show_xml, show_json, show_xml_by_id, show_json_by_id
from wishlist.views import register, login_user, logout_user
from wishlist.views import show_wishlist_ajax, add_wishlist_ajax

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/', show_wishlist_ajax, name='show_wishlist_ajax'),
    path('ajax/submit/', add_wishlist_ajax, name='add_wishlist_ajax')
]