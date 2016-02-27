from django.contrib import admin

# Register your models here.
from .models import Contact
from .forms import ContactForm

class ContactAdmin(admin.ModelAdmin):
	list_display =("__str__","message")
	form = ContactForm
	# class Meta:
	# 	model = SignUp

		
admin.site.register(Contact,ContactAdmin)