from django.shortcuts import render

# Create your views here.
def UserProfile(request):
	title = 'Welcome' 
	context = {  
	"title": title,
	
	}
	return render(request,"profile.html",context)