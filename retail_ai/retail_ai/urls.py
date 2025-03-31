from django.contrib import admin
from django.urls import path, include  # include is used to include app-specific URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include the accounts app URLs
]
