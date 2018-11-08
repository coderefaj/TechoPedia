from .models import *

user_login_url='/users/login'
timeout_seconds = 2
extension_lang = {
	"python" : ".py",
	"gcc" : ".c",
	"c++" : ".cpp" ,
	"javac" : ".java" ,
}

def get_problem_objects():
	return Problem.objects.all()

def get_problem_objects_by_id(id):
	return Problem.objects.get(id=id)

def get_attempted_problems(user,id):
	return problem_attempted.objects.get(user=user,problem=id)

def get_time_of_user(user):
	return Time.objects.get(user=user)

def get_sample_testcase(queryset):
	return Testcase.objects.filter(problem=queryset,
											sample=True)

def get_marks_for_problem(user,problem):
	return Problem_marks.objects.get(user=user,problem=problem)

def get_marks_for_user(user):
	return Marks.objects.get(user=user)

def get_all_testcase(id):
	return Testcase.objects.filter(problem=id)

def get_user_code(user):
	return UserCode.objects.get(user=user)