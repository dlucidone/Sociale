from django.db import models

# Create your models here.
class Contact(models.Model):
	
	full_name = models.CharField(max_length = 120,blank = False, null = True)
	email = models.EmailField()
	message = models.CharField(max_length = 1000,blank = False, null = True) 
	

	def __str__(self):
		return self.full_name
		
