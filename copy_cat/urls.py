from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include("forum.urls", namespace="forum"))
]

# Glad we are switching away from urls to path which the newer Django version has