from rest_framework import serializers
from menu.models import menulist

class menulistSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()
    detail = serializers.HyperlinkedIdentityField(
        view_name='menu-url:detail'
    )

    class Meta:
        model = menulist
        fields =('seller', 'menu', 'price', 'expires', 'aval', 'menuPic', 'detail')

    def get_seller(self, obj):
        return str(obj.seller.BrandName)



class menudetailSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()

    class Meta:
        model = menulist
        fields = '__all__'

    def get_seller(self, obj):
        return str(obj.seller.BrandName)





