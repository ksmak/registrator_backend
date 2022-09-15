from django.urls import path, include
from rest_framework import routers
from . import views, services 

router = routers.DefaultRouter()
router.register('', services.UserRequestViewSet, basename='UserRequest')

urlpatterns = [
    path('get_addr_list/', views.get_addr_list, name='user-requests-get-addr-list'),
    path('print/', views.print_vedomost, name='user-requests-print-vedomost'),
    path('send/', views.send_vedomost, name='user-requests-send-vedomost'),
    path('get_dicts/', views.get_all_dictionaries, name='user-requests-get-dicts'),
    path('check_iin/', views.check_iin, name='user-requests-check-iin'),
    path('check_phone/', views.check_phone, name='user-requests-check-phone'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]