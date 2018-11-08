from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import ListView,DetailView
from .models import Problem , Testcase , Time , problem_attempted , Problem_marks ,Marks ,UserCode
#for compiling
import shlex
from subprocess import Popen, PIPE , check_output
import subprocess
from threading import Timer
import json
import curses
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .helper import *

class problem_list(LoginRequiredMixin,ListView):
	model = Problem
	login_url = user_login_url
	redirect_field_name = 'redirect_to'
	template_name = 'problem_list.html'
	def get_context_data(self,**kwargs):
		context = super(problem_list,self).get_context_data(**kwargs)
		context['prblm_list'] = get_problem_objects()
		return context

@login_required(login_url=user_login_url)
def index(request,id):
	if request.method == "GET":
		context = {}
		# print(request.user.id)
		queryset = get_problem_objects_by_id(id)
		total = get_problem_objects()
		status_ =  get_attempted_problems(request.user,id)
		context['problem']  = queryset
		context['total'] = total
		testcase_inp =[x.input_file.read().decode("ASCII") for x in Testcase.objects.filter(problem=queryset,sample=True) ]
		context['time'] = get_time_of_user(request.user)
		testcase_out = [x.output_file.read().decode("ASCII") for x in Testcase.objects.filter(problem=queryset,sample=True) ]
		test_case = get_sample_testcase(queryset)
		context['test_case'] = zip(testcase_inp,testcase_out)
		context['code'] = send_source_code(request.user)
		template_name = 'code.html'
		return render(request,template_name,context)

def run_it(cmd, timeout_sec , input_ ,user_output , output_case):
	result = {}
	#output_ is for proc
	output_ = open(user_output,"w")
	proc = Popen(shlex.split(cmd),stdin = input_ , stdout = output_ , stderr=PIPE)
	timer = Timer(timeout_sec , proc.kill)
	try:
		timer.start()
		stdout , stderr = proc.communicate()
	finally:
		timer.cancel()
	output_.close()
	#now to check for equality of user generated file and testcase
	output = open(user_output,'r')
	# print ("output check",output_check)
	# print ("output",output.readlines())
	output_data = output.read()
	if ( output_data == output_case):
		result['pass'] = True
		result['stderr'] = stderr.decode("utf-8")
	else:
		result['pass'] = False
		error = "Expected output "+output_case+" But Obtained "+output_data
		result['stderr'] = error
	result['stdout'] = str(output_data)
	print ("generated output ",output_data)

	output.close() # file is closed
	print (result)
	# print("FRom run it ", result)
	return result

# Used for compilation process
def execute(cmd):
	proc = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)
	stdout, stderr = proc.communicate()
	result = {}
	result['stdout'] = stdout.decode("utf-8")
	result['stderr'] = stderr.decode("utf-8")
	print (stderr.decode('utf-8'))
	final = {}
	final['case_1'] = result
	return final

def compile_it_please(filename,code_lang,input_file,output_file,username):
	binary_file_name = (filename.split("."))[0]
	if (code_lang!="javac"):
		cmd = code_lang + " "+filename +" -o " + binary_file_name
	else :
		cmd = "javac "+filename
	print (cmd)
	timeout_sec = timeout_seconds  #timeout for handling infilite loop
	result = execute(cmd)
	# print (result)
	# to check for any errors in compilation process
	if(len(result["case_1"]['stderr'])<2):
		if(code_lang!="javac"):
			cmd = "./"+binary_file_name #for c and c++
		else:
			cmd = "java "+ binary_file_name # for java
		# print (cmd)
		final = {}
		case_level = 0
		for file in input_file:
			input_ = open(file) # input file name
			user_output = username+"_output.txt" # file to store user gen output
			output_case = open( (output_file[case_level]) ) # output case file in our system
			# print ("output case ","ghgh", output_case.read())
			output_case = output_case.read()

			result = run_it(cmd , timeout_sec , input_ , user_output , output_case)
			case_level = case_level + 1
			final['case_'+str(case_level)] = result
			# print ("compile it please ",result)
		# print (final)
		return final
	else:
		return result

def run(request,id):
	if request.method == "POST":
		attempted = get_attempted_problems(request.user,id)
		if(not (attempted.status)):
			attempted.status = True
			attempted.save()
		username = request.user.username
		programming_lang = request.POST['programming_lang']
		extension = extension_lang[programming_lang]
		test_case_files = get_sample_testcase(id)
		#collecting input file list
		local_sys = '/home/Incogntio2K18devnation/DevNation'
		input_file = [ local_sys+x.input_file.url for x in test_case_files]
		output_file = [ local_sys+x.output_file.url for x in test_case_files]
		filename = username+"_problem_"+str(id)+extension
		# print (filename)
		fopen = open(filename,"w")
		code = request.POST['code']
		fopen.write(code)
		fopen.close()
		result = compile_it_please(filename,programming_lang,input_file,output_file,username)
		jsons = json.dumps(result)
		template_name = 'code.html'
		return HttpResponse(jsons)

def allocate_marks(result,user,problem):
	prblm_mrk = get_marks_for_problem(user,problem)
	total_cases = len(result)
	prblm_mrk.marks = 0
	prblm_mrk.save()
	for itr in range(total_cases):
		if(result["case_"+str(itr+1)]["pass"] == True):
			prblm_mrk.marks = prblm_mrk.marks + 2
			print (prblm_mrk.marks)
			prblm_mrk.save()
			# print ("done")

def total_marks(user):
	problem = get_problem_objects()
	total_problems = len(problem)
	marks_ = get_marks_for_user(user=user)
	marks_.marks = 0
	marks_.save()
	for itr in range(total_problems):
		try:
			prblm_mrk = get_marks_for_problem(user,problem[itr])
			marks_.marks = marks_.marks + prblm_mrk.marks
			marks_.save()
		except Exception as e:
			print ("[-] ",e)

def submit(request,id):
	if request.method == "POST":
		username = request.user.username
		programming_lang = request.POST['programming_lang']
		extension = extension_lang[programming_lang]
		test_case_files = get_all_testcase(id)
		local_sys = '/home/Incogntio2K18devnation/DevNation'
		input_file = [ local_sys+x.input_file.url for x in test_case_files]
		output_file = [ local_sys+x.output_file.url for x in test_case_files]
		filename = username+"_problem_"+str(id)+extension
		# print (filename)
		fopen = open(filename,"w")
		code = request.POST['code']
		fopen.write(code)
		fopen.close()
		result = compile_it_please(filename,programming_lang,input_file,output_file,username)
		allocate_marks(result,request.user,id)
		total_marks(request.user)
		jsons = json.dumps(result)
		template_name = 'code.html'
		return HttpResponse(jsons)

def time_it(request):
	if request.method=="POST":
		minutes = request.POST['minutes']
		seconds = request.POST['seconds']
		tm = get_time_of_user(request.user)
		tm.minutes = minutes
		tm.seconds = seconds
		tm.save()
		return HttpResponse("done")

def save_user_code(request):
	if request.method=="POST":
		uc = get_user_code(request.user)
		code = request.POST['code']
		uc.source_code = code
		uc.save()
		return HttpResponse("done")

def send_source_code(user):
	uc = get_user_code(user)
	code = uc.source_code
	return (code)
