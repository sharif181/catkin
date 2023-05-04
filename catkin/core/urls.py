from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('authentication.urls')),
    path('our-team/', include('our_team.urls')),
    path('review/', include('client_review.urls')),
    path('contact/', include('contact_us.urls')),
    path('slider/', include('homepage_slider.urls')),
    path('promotion/', include('promotion.urls')),
    path('service/', include('service.urls')),
    path('project/', include('catkin_project.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
