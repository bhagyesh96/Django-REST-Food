from .serializers import menulistSerializer, menudetailSerializer
from menu.models import menulist
from rest_framework import generics
from django.db.models import Q

class menuList(generics.ListAPIView):
    #queryset = menulist.objects.all()
    serializer_class = menulistSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = menulist.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(cuisin__icontains=query)|
                Q(menu__icontains=query)|
                Q(seller__Address__icontains=query)|
                Q(seller__BrandName__icontains=query)|
                Q(seller__city__icontains=query)
            ).distinct()
        return queryset_list


class menuDetail(generics.RetrieveAPIView):
    queryset = menulist.objects.all()
    serializer_class = menudetailSerializer








