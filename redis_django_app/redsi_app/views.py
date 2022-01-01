import json
import random

from redsi_app.models import Product

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.core.cache import cache
from django.conf import settings
# from django.core.cache.backends.base import DEFAULT_TIMEOUT

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@api_view(['GET', 'POST'])
def manage_items_redis(request, *args, **kwargs):
        number = random.randint(1, 100)
        key = f'efood.region.{number}'
        value = json.loads(request.body)
        print("value.................", value)
        cache.set(key, value)
        print("cache........", cache.get(key))
        # items = json.loads(request.body)
        # for key in list(items.keys()):
        #     value = items[key]
        #     cache.set(key, value)

        response = {
            'msg': f"successfully added value to redis"
        }
        return Response(response, 201)


# @api_view(['GET', 'PUT', 'DELETE'])
# def manage_item(request, *args, **kwargs):
#
#     print(kwargs['key'])
#     if request.method == 'GET':
#         key = f"efood.region.{kwargs['key']}"
#         if key:
#             value = cache.get(key)
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
#
#
# @api_view(['GET'])
# def view_cached_books(request, *args, **kwargs):
#     # if 'efood.region' in cache:
#         # get results from cache
#     products = cache.get('efood.region.*')
#     print(products)
#     return Response(products, status=status.HTTP_201_CREATED)
#
#     # else:
#     #     products = Product.objects.all()
#     #     results = [product.to_json() for product in products]
#     #     # store data in cache
#     #     cache.set('product', results)
#     #     return Response(results, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET'])
# def get_values_redis(request, *args, **kwargs):
#
#     items = {}
#     count = 0
#     print(cache.keys("/*"))
#     for key in cache.keys("*"):
#         items[key] = cache.get(key)
#         count += 1
#     response = {
#         'count': count,
#         'msg': f"Found {count} items.",
#         'items': items
#     }
#     return Response(response, status=200)
#
#
# @api_view(['GET'])
# def delete_from_redis(request, *args, **kwargs):
#
#     print(kwargs)
#     key = f"efood.region.{kwargs['key']}"
#     if key:
#         data = cache.delete(key)
#     response = {
#         'msg': f"successfully deleted from redis, key is {key}",
#     }
#     return Response(response, status=204)



