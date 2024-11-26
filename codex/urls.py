from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls', namespace='core')),
    path('hotel/', include('hotel.urls', namespace='hotel')),
    path('restaurant/', include('restaurant.urls', namespace='restaurant')),
    path('supermarket/', include('supermarket.urls', namespace='supermarket')),
    path('users/', include('users.urls', namespace='users')),
    path('billing/', include('billing.urls', namespace='billing')),
    path('rappel/', include('rappel.urls', namespace='rappel')),
]
