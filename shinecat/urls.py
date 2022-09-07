from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from blog.views import frontpage, post_detail,technical,subscribe,hotpost,lifehacks,science,entertainment,help

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('see/<slug:slug>/', post_detail, name='post_detail'),
    path('technical_blog',technical),
    path('story',hotpost),
    path('entertainment',entertainment),
    path('lifehacks',lifehacks),
    path('science',science),
    path('subscribe',subscribe),
    path('help',help),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

