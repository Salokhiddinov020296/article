from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

]
urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    path('post/', include('post.urls')),
    path('author/', include('author.urls'))
)

handler404 = "post.views.page_not_found_view"
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
