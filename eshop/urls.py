
from django.contrib import admin
from django.urls import path, include
from django.conf import settings #var media and..
#it helps to make url path
from django.conf.urls.static import static #connection between base root and static files especially medias

urlpatterns = [
    #Admin url
    path('admin/', admin.site.urls),

    #Store app
    path('', include('store.urls')), #here we connect urls from store to project

    #Cart app
    path('cart/', include('cart.urls')),

    #Account app
    path('account/', include('account.urls')),

    #Payment app
    path('payment/', include('payment.urls')),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)      #MEDIA_URL this is why we imported settings we can connect to var we imported

