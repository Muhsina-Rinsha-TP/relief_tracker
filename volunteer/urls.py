from django.urls import path
from .views import volunteer_home, update_delivery

urlpatterns = [
    path('', volunteer_home, name='volunteer_home'),
    path('update/<int:item_id>/', update_delivery, name='update_delivery'),
]
