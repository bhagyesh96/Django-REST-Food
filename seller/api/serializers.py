from rest_framework import serializers
from seller.models import sellerDetails

class sellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = sellerDetails
        fields = '__all__'
        #fields = ('username', 'email', 'Address', 'PhoneNo')










