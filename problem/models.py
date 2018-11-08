from django.db import models
from users.models import CustomUser

#for populating the db
from django.db.models.signals import post_save
from django.dispatch import receiver
from devnation import settings

class Problem(models.Model):
	name  = models.CharField(max_length=100,blank=False)
	statement  = models.TextField()
	# source_code = models.FileField(upload_to="source/")
	def __str__(self):
		return self.name

class UserCode(models.Model):
	user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
	source_code = models.TextField(blank=True, null=True)

class Time(models.Model):
	user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	minutes = models.IntegerField(max_length=90,default=89)
	seconds = models.IntegerField(max_length=60,default=59)



class Testcase(models.Model):
	problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
	input_file = models.FileField(upload_to="input/")
	output_file = models.FileField(upload_to="output/")
	# input_case = models.TextField(blank=True, null=True)
	# output_case = models.TextField(blank=True, null=True)
	sample = models.BooleanField(default=False)



class Problem_marks(models.Model):
	user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
	marks = models.IntegerField(default=0)
	def __str__(self):
		return self.user.username

class Marks(models.Model):
	user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	marks  = models.IntegerField(default=0)
	def __str__(self):
		return self.user.username


class problem_attempted(models.Model):
	user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
	status = models.BooleanField(default=False)


@receiver(post_save, sender=CustomUser)
def status_new_user(instance, created, raw, **kwargs):
	# raw is set when model is created from loaddata.
	if created and not raw:
	    # instance.groups.add(
	    #     Group.objects.get(name='new-user-group'))

	    # Category.objects.create(
	    #     name="Default", user=instance)

	    # Feed.objects.create(
	    #     user = instance,
	    #     name = "%s's Feed" % instance.first_name,
	    #     ....
	    # )
		default_content = "WELCOME TO DEVNATION"
		UserCode.objects.create(user=instance,source_code=default_content)
		Time.objects.create(user=instance,minutes=89,seconds=59)
		Marks.objects.create(user=instance,marks=0)
		total_problems = Problem.objects.all()
		for prob in total_problems:
			problem_attempted.objects.create(user=instance , problem = prob, status = False)
			Problem_marks.objects.create(user=instance , problem = prob , marks = 0)