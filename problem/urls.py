from django.urls import path
from .views import *

urlpatterns = [
	path('', problem_list.as_view() , name='problem_list'),
    path('ques/<int:id>/', index , name='problem'),
    path('ques/<int:id>/execute',run,name='run'),
    path('ques/<int:id>/submit',submit ,name='submit'),
    path('timeit',time_it,name='time_it'),
    path('save',save_user_code,name="save_code"),
    path('source_code',send_source_code,name="send_source_code"),

]
