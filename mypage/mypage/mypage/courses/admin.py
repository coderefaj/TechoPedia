from django.contrib import admin
from .models import GitCours
from .models import LinuxCours
from .models import PyCours
from .models import JsCours
from .models import JqCours
from .models import MyCours


# Register your models here.
admin.site.register(GitCours)
admin.site.register(LinuxCours)
admin.site.register(PyCours)
admin.site.register(JsCours)
admin.site.register(JqCours)
admin.site.register(MyCours)
