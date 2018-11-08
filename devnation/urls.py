from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('problem/', include('problem.urls')),
    path('users/', include('django.contrib.auth.urls')),
    # path('times/', include('problem.urls')),
]

handler404 = 'users.views.handler404'
handler500 = 'users.views.handler500'