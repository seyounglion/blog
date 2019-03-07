from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
import accounts.views
from django.conf import settings #미디어
from django.conf.urls.static import static #미디어

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('main/',blogapp.views.main, name="main"),
    path('blog/', include('blogapp.urls')),
    #path('blog/<int:blog_id>',blogapp.views.detail, name="detail"),
    #path('blog/new/', blogapp.views.new, name="new"),
    #path('blog/create',blogapp.views.create, name="create"),
    path('portfolio/', include('portfolio.urls')),
    #path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('accounts/', include('accounts.urls')),
    #path('accounts/login/', accounts.views.login, name="login"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #미디어 


