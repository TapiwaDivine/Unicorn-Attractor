"""unicorn_attractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static
from home import urls as urls_home
from services import urls as services_urls
from issue_tracker import urls as issues_urls
from accounts import urls as accounts_urls
from cart import urls as urls_cart
from checkout import urls as urls_checkout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='home/')),
    url(r'^home/', include('home.urls')),
    url(r'^services/', include(services_urls)),
    url(r'^issue_tracker/', include(issues_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    #url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
