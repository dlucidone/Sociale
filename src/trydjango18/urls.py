from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contact/', 'contact.views.Contact', name='Contact'),
    url(r'^about/', 'newsletter.views.About', name='About'),
    url(r'^profile/', 'UserProfile.views.UserProfile', name='UserProfile'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'^thirdauth/$', 'thirdauth.views.home', name='home'),
    url(r'^thirdauth/fblogin/$', 'fb.views.Userlogin', name='Userlogin'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

   ]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)