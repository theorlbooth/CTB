from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/beers/', include('beers.urls')),
    path('api/sales/', include('sales.urls')),
    path('api/auth/', include('jwt_auth.urls'))
]
