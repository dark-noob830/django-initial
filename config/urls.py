from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('', include('home.urls')),
    path('book/', include('book.urls')),
    path('user/', include('user_info.urls')),
    path('comments/', include('comments.urls')),
    path('book-actions/', include('book_actions.urls')),
    path('tag/', include('tag.urls')),
    path('forum/', include('forum.urls')),
    path('advance/', include('adv_search.urls')),
    path('chat/', include('chat.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
])

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
