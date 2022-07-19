from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    path('meals/', include('meals.urls', namespace='abomealsuts')),
    path('reserve_table/', include('reservation.urls', namespace='reservation')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('abouts/', include('abouts.urls', namespace='aboutus')),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('', include('home.urls', namespace='home')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



