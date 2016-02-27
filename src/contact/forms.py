from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['full_name','email','message']
		#exclude=['email']  #use sparinglyyyy

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base,provider = email.split("@")
		domain, extension = provider.split('.')
		if not domain.lower() == 'gmail': 
			raise forms.ValidationError("Please make sure you use your gmail email.")
		if not extension.lower() == "com":
			raise forms.ValidationError("Please use a valid .com email address")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name

	def clean_message(self):
		message = self.cleaned_data.get('message')
		return message