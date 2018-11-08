from django.contrib import admin
from .models import * 

class TestcaseInline(admin.TabularInline):
	model = Testcase

class ProblemAdmin(admin.ModelAdmin):
	inlines = [
			TestcaseInline,
				]
class ProblemMarksAdmin(admin.ModelAdmin):
	model = Problem_marks
	list_display = ['user','problem','marks']

class MarksAdmin(admin.ModelAdmin):
	model = Marks 
	list_display = ['user','marks']
	ordering = ['marks']

admin.site.register(Problem_marks,ProblemMarksAdmin)
admin.site.register(Marks,MarksAdmin)
# admin.site.register(ProblemAdmin,Problem)
admin.site.register(Problem,ProblemAdmin)
admin.site.register(UserCode)
# admin.site.register(Marks,P)
admin.site.register(Time)
admin.site.register(problem_attempted)
# admin.site.register(Problem_marks)