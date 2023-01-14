from selling.models import SellingPost
from rest_framework import serializers
from authentication.models import User
from authentication.serializers import UserSerializer

class SellingPostSerializer(serializers.ModelSerializer):
    #seller = UserSerializer(many=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)
    class Meta:
        model = SellingPost
        fields = ('title', 'content')

    def create(self, validation_data):
        print('validation data ', validation_data)
        return SellingPost.objects.create_post(**validation_data)