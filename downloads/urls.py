from django.urls import path, include
from downloads import views

app_name = 'downloads'

urlpatterns = [
    path('census',views.download_census, name='census'),
]