from django.urls import path
from .views import view_cached_books, manage_items_redis, manage_item

app_name = 'redis_api'

urlpatterns = [
    path('products_cache/', view_cached_books, name="books"),
    path('items/', manage_items_redis, name="items"),
    path('<slug:key>/', manage_item, name="single_item"),
]
