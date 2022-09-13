from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from blog.views import frontpage, post_detail,technology,subscribe,testing,djangotopic,software,python,help

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('see/<slug:slug>/', post_detail, name='post_detail'),
    path('technology',technology),
    path('django',djangotopic),
    path('python',python),
    path('software',software),
    path('testing',testing),
    path('subscribe',subscribe),
    path('help',help),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

