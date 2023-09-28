"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.conf import settings


from django.contrib import admin
from django.urls import path , include 
# for render.com to deplay 

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('books.urls')),

    path('', include('users.urls')),
    path('', include('carts.urls')),
    path('', include('search.urls')),
    path('', include('wishlist.urls')),
    path('', include('order.urls')),
    path('', include('tools.urls')),
    path('', include('admin_page.urls')),
    path('', include('comments.urls')),
    path('', include('quotes.urls')),    
    path('', include('rating.urls')),
    path('', include('follow.urls')),
    path('', include('chat.urls')),
    # path('', include('adds.urls')),
    path('', include('apis.urls')),
    path('', include('archive.urls')),
    
    
    
    
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

# handler404 = 'core.views.error_404_view'