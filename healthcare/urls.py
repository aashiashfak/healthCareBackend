from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('custom_admin/',include('custom_admin.urls')),
    path('patient/',include('patient.urls')),
    path('hospital/',include('hospital.urls')),
] 

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    

