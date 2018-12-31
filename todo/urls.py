from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('delete/<list_id>',views.delete_item,name='delete'),
    path('edit/<list_id>',views.edit_item,name='edit'),
    path('crossed/<list_id>',views.crossed_item,name='crossed'),
    path('uncrossed/<list_id>',views.uncrossed_item,name='uncrossed'),
]
