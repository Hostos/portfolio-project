from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'), #name='home' is so you can call it by 'home' elsewhere in the app? I think like url 'home'
    path('blog/', include('blog.urls')), #the blog in blog.urls has to be the name of the app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
