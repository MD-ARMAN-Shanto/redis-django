import json

from redsi_app.models import Product

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# @api_view(['GET', 'POST'])
# def manage_items(request, *args, **kwargs):
#     if request.method == 'GET':
#         items = {}
#         count = 0
#         for key in cache.keys("*"):
#             print(key)
#             items[key] = cache.get(key)
#             count += 1
#         response = {
#             'count': count,
#             'msg': f"Found {count} items.",
#             'items': items
#         }
#         return Response(response, status=200)
#     elif request.method == 'POST':
#         items = json.loads(request.body)
#         for key in list(items.keys()):
#             value = items[key]
#             cache.set(key, value)
#
#         response = {
#             'msg': f"successfully added value to redis"
#         }
#         return Response(response, 201)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def manage_item(request, *args, **kwargs):
#
#     print(kwargs)
#     if request.method == 'GET':
#         if kwargs['key']:
#             value = cache.get(kwargs['key'])
#             if value:
#                 response = {
#                     'key': kwargs['key'],
#                     'value': value,
#                     'msg': 'success'
#                 }
#                 return Response(response, status=200)
#             else:
#                 response = {
#                     'key': kwargs['key'],
#                     'value': None,
#                     'msg': 'Not found'
#                 }
#                 return Response(response, status=404)
#     elif request.method == 'PUT':
#         if kwargs['key']:
#             request_data = json.loads(request.body)
#             new_value = request_data['new_value']
#             value = cache.get(kwargs['key'])
#             if value:
#                 cache.set(kwargs['key'], new_value)
#                 response = {
#                     'key': kwargs['key'],
#                     'value': value,
#                     'msg': f"Successfully updated {kwargs['key']}"
#                 }
#                 return Response(response, status=200)
#             else:
#                 response = {
#                     'key': kwargs['key'],
#                     'value': None,
#                     'msg': 'Not found'
#                 }
#                 return Response(response, status=404)
#
#     elif request.method == 'DELETE':
#         if kwargs['key']:
#             result = cache.delete(kwargs['key'])
#             if result == 1:
#                 response = {
#                     'msg': f"{kwargs['key']} successfully deleted"
#                 }
#                 return Response(response, status=404)
#             else:
#                 response = {
#                     'key': kwargs['key'],
#                     'value': None,
#                     'msg': 'Not found'
#                 }
#                 return Response(response, status=404)


@api_view(['GET'])
def view_cached_books(request):
    if 'product' in cache:
        # get results from cache
        products = cache.get('product')
        return Response(products, status=status.HTTP_201_CREATED)

    else:
        products = Product.objects.all()
        print(products)
        results = [product.to_json() for product in products]
        # store data in cache
        cache.set('product', results, timeout=CACHE_TTL)
        return Response(results, status=status.HTTP_201_CREATED)
