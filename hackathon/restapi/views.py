# -*- coding: utf-8 -*-

from django_filters.rest_framework import DjangoFilterBackend

from django.contrib.auth.models import User, Group
from django.db.models import Q

from rest_framework import viewsets, generics, pagination
from serializers import *

from hackathon.models import *
import datetime



# class CatalogItemViewSet(viewsets.ModelViewSet):
#     serializer_class = CatalogItemSerializer
#     pagination_class = pagination.LimitOffsetPagination

#     def get_serializer_class(self):
#         if self.request.query_params.get('search', None) is not None:
#             return CatalogItemSearchSerializer
#         elif self.request.query_params.get('with_value', None) is not None:
#             return CatalogItemWithValueSerializer
#         else:
#             return CatalogItemSerializer

#     def get_queryset(self):
#         queryset = CatalogItem.objects.all()

#         to_order = self.request.query_params.get('to_order', None)
#         search = self.request.query_params.get('search', None)
#         articul = self.request.query_params.get('articul', None)
#         foreign_id = self.request.query_params.get('foreign_id', None)
#         section = self.request.query_params.get('section', None)
#         store = self.request.query_params.get('store', None)
#         item_name = self.request.query_params.get('item_name', None)

#         with_nested_section = self.request.query_params.get('with_nested_sections', None)

#         if with_nested_section and section:
#             section_obj = CatalogSection.objects.get(pk=section)
#             sections = section_obj._children_recursive_flat(section_obj,1)
#             sections.append(section_obj)
#             section = None
#             queryset = queryset.filter(section__in=sections)
        
#         if search is not None:
#             if search.isdigit():
#                 filter = Q(name__icontains=search) | Q(foreign_id=search) | Q(articul=search)
#             else:
#                 chunks = search.split(' ')
#                 filter = Q(pk__gte=0)
#                 for chunk in chunks:
#                     filter = filter & Q(name__icontains=chunk) | Q(articul=search)
#             queryset = queryset.filter(filter)
#             return queryset

#         if articul is not None:
#             queryset = queryset.filter(articul=articul)
#         if foreign_id is not None:
#             queryset = queryset.filter(foreign_id=foreign_id)
#         if section is not None:
#             queryset = queryset.filter(section_id=section)
#         if item_name is not None:
#             chunks = item_name.split()            
#             filter = Q(pk__gte=0)
#             for chunk in chunks:
#                 filter = filter & Q(name__icontains=chunk)
#             queryset = queryset.filter(filter)
#         if to_order is not None:

#             pass

#             # queryset = queryset.filter(order_goods__deficit__gt=0, order_goods__order__status='ORDERED').distinct()
#             # exclude_goods = []
#             # for good in queryset:
#             #     if good.reserve - good.remains - good.ordered_already <= 0:
#             #         exclude_goods.append(good.id)
#             # queryset = queryset.exclude(pk__in=exclude_goods)

#         if store is not None:
#             queryset = queryset.filter(stores_existance__count__gt=0, stores_existance__store=store)

#         return queryset



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

