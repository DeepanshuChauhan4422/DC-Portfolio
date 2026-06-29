"""
URL configuration for portfolio_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls', namespace='portfolio')),
    
    # SEO Files
    path('sitemap.xml', TemplateView.as_view(template_name='portfolio/sitemap.xml', content_type='text/xml')),
    path('robots.txt', TemplateView.as_view(template_name='portfolio/robots.txt', content_type='text/plain')),
]

# Serve media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
