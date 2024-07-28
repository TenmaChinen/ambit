from django.urls import path, include
from colonies import views

app_name = 'colonies'

urlpatterns = [
    path('list/',views.list_view, name='list'),
    path('create/',views.create_view, name='create'),
    path('detail/<int:pk>',views.detail_view, name='detail'),
    path('update/<int:pk>',views.update_view, name='update'),
    path('delete/<int:pk>',views.delete_view, name='delete'),
]