from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from post.sitemaps import ArticleSitemap
from post.views import PostDetailView


sitemaps = {'articles': ArticleSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name='detail'),

]
urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    path('post/', include('post.urls')),
    path('author/', include('author.urls'))
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
