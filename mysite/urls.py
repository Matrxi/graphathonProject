from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin, auth
from mysite.core import views as core_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', core_views.homewelcome, name='homewelcome'),
    url(r'^home/$', core_views.home, name='home'),
    url(r'^welcome/$', core_views.homewelcome, name='homewelcome'),
    url(r'^contact/$', core_views.contact, name = 'contact'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^form/$', core_views.model_form_upload, name='model_form_upload'),
    url(r'^files/$', core_views.uploaded_files, name='uploaded_files'),
    url(r'^deleteOne/$', core_views.delete_first_file, name = 'delete_first_file'),
    url(r'^deleteAll/$', core_views.delete_all_files, name = 'delete_all_files'),
    url(r'^filer/', include('filer.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
