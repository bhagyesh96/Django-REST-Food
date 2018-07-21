from .serializers import sellerSerializer
from seller.models import sellerDetails
from rest_framework import mixins
from rest_framework import generics
from rest_framework.parsers import JSONParser

'''class sellerList(APIView):

    def get(self, request):
        seller = sellerDetails.objects.all()
        serialize = sellerSerializer(seller, many=True)
        #serialize = json.load(serialize)
        return Response(serialize.data)

    def post(self, request):
        pass'''

'''class sellerList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = sellerDetails.objects.all()
    serializer_class = sellerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)'''


class sellerList(generics.ListCreateAPIView):
    parser_classes = (JSONParser,) #include in every create methon of rest api
    queryset = sellerDetails.objects.all()
    serializer_class = sellerSerializer


class sellerDetail(generics.RetrieveAPIView):
    queryset = sellerDetails.objects.all()
    serializer_class = sellerSerializer























