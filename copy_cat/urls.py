from django.conf.urls import include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('r/', include('forum.urls')),
    path('u/', include('user.urls')),
    # Can alter later depending on page design
    path('', include('log_reg.urls'))
]
