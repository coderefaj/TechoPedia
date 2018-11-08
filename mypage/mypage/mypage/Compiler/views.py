from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Compiler
import subprocess
from subprocess import Popen , PIPE , STDOUT

def index(request):
	if(request.method == 'POST'):
		output=''
		txt = request.POST['txt']
		txt = txt
		# program = request.POST['program']
		comp = Compiler(txt=txt)
		comp.save()
		fopen = open("temp.py",'w+')
		fopen.write(txt)
		fread = fopen.read()
		for line in fread:
			print line
		try:
			print subprocess.check_output("cp /home/python4all/mypage/temp.py /home/python4all/mypage/static",shell=True)
                        c = subprocess.check_output("python temp.py",shell=True)
	               # print subprocess.check_output("cp /home/python4all/mypage/temp.py /home/python4all/mypage/mypage/Compiler/static",shell=True)
        # c = subprocess.check_output("gcc temp.c",shell=True)
			# c = subprocess.

			output = c
			context = {'output':c,'txt':txt,}
		except:

			cmd = 'python temp.py'
			p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
			# cmd = './a.out'
			# p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

			output = p.stdout.read()
			context = {'output':output,}
		return render(request,'index1.html',context)
	else:
		return render(request,'index1.html')
