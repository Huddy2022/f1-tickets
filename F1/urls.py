from django.contrib import admin
from django.urls import path, include
from Tickets.views import CreateCheckoutSessionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Tickets.urls'), name='Tickets_urls'),
    path('accounts/', include('allauth.urls')),
    path('create-checkout-session',
         CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
