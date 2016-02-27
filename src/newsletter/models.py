from django.db import models

# Create your models here.
class SignUp(models.Model):
	
	full_name = models.CharField(max_length = 120,blank = False, null = True)
	email = models.EmailField() 
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __str__(self):
		return self.email
		
