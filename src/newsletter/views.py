from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def home(request):
	title = "Welcome"
	# if request.user.is_authenticated():
	#  	title = "Welc ome User %s" %(request.user)
	form  = SignUpForm(request.POST or None)
	context = {  
	"title": title,
	"form":form
	}

	if form.is_valid():
		#form.save()
		#print(request.POST['email']) #not a good practice to get post datw
		instance = form.save(commit = False)
		# full_name = form.cleaned_data.get('full_name')
		# if not full_name:
		# 	full_name = "new Name"
		# instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name == 'Justin'
		
		
		instance.save()
		context = {
		"title":"THANK YOU"
		}
		# print(instance.email)



 
	


	return render(request,"index.html",context)



def About(request):
	return render(request,"about.html")