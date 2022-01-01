from django.urls import path
from .views import view_cached_books, manage_items_redis, manage_item, get_values_redis, delete_from_redis

app_name = 'redis_api'

urlpatterns = [
    path('products_cache/', view_cached_books, name="books"),
    path('redis_get_values/', get_values_redis, name="get_redis_items"),
    path('items/', manage_items_redis, name="items"),
    path('redis_single_item/<slug:key>/', manage_item, name="single_item"),
    path('redis_delete_item/<slug:key>/', delete_from_redis, name="delete_single_item"),
]
