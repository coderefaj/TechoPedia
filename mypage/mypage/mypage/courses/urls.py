from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'PythonCompiler.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.courses, name="courses"),
    url(r'git/', views.githome , name="githome"),
    url(r'linux/', views.linuxhome , name="linuxhome"),
    url(r'python/', views.pyhome , name="pyhome"),
    url(r'js/', views.jshome , name="pyhome"),
    url(r'jquery/', views.jqueryhome , name="pyhome"),
    url(r'mysql/', views.mysqlhome , name="pyhome"),


]
