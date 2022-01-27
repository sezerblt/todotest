from django.urls import path
from . import views

urlpatterns = [
    path('',views.index1, name='url-index'),
    path('create/',views.create, name='url-create'),
    path('context/<int:id>',views.context, name='url-context'),
    path('update/<int:id>/', views.update, name='url-update'),
    path('delete/<int:id>/', views.delete, name='url-delete'),
]