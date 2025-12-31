from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('donor/', include('donor.urls')),
    path('volunteer/', include('volunteer.urls')),
]
