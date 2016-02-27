from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def Contact(request):
	title = "Contact Us"
	form  = ContactForm(request.POST or None)
	context = {  
	"title": title,
	"form":form
	}

	if form.is_valid():
		instance = form.save(commit = False)
		form_email = form.cleaned_data.get('email')
		form_message = form.cleaned_data.get('message')
		form_full_name = form.cleaned_data.get('full_name')

		subject = 'Site Contact Form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,'jackravi227@gmail.com']
		contact_message = ("%s:%s via %s"%(
			form_full_name,
			form_message,
			form_email
			))
		some_html_message = """
		<h1>Hello</h1>
		"""
		# send_mail(subject,
		# 	contact_message,
		# 	from_email,
		# 	to_email,
		# 	html_message = some_html_message,
		# 	fail_silently = False)
		
		send_mail(subject, contact_message, from_email, ['jackravi227@gmail.com'], fail_silently=False)
		instance.save()
		context = {
		"title":"THANK YOU"
		
		}



 
	


	return render(request,"contact.html",context)


	