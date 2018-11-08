from django.contrib import admin

# Register your models here.
from .models import profile , course_name


class profileAdmin(admin.ModelAdmin):
	class Meta:
		model=profile
admin.site.register(profile, profileAdmin)
admin.site.register(course_name)
