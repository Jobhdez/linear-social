from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('chat/', include('chat.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
