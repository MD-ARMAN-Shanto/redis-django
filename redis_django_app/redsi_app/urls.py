from django.urls import path
from .views import manage_items, manage_item

app_name = 'redis_api'

urlpatterns = [
    path('items/', manage_items, name="items"),
    path('<slug:key>/', manage_item, name="single_item")
]