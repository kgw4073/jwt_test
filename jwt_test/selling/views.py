from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication
import jwt
from django.conf import settings

import json, re

from selling.serializers import SellingPostSerializer
from selling.models import SellingPost
from selling.renderers import UserJSONRenderer

from .models import User
# Create your views here.
class SellingPostView(APIView):
    permission_classes = (AllowAny, )
    renderer_classes = (UserJSONRenderer,)
    serializer_class = SellingPostSerializer

    def post(self, request):
        auth_header = authentication.get_authorization_header(request).split()
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')
        payload = jwt.decode(token, settings.SECRET_KEY)
        seller_id = payload['id']
        print('sellsei ', id)
        seller = User.objects.get(pk=seller_id)

        selling_post = SellingPost(seller, 'galaxy', 'selilng lgalyc 4')
        # selling_post.seller = seller
        # selling_post.title = 'galaxy',
        # selling_post.content = 'selling galaxy watch 4'
        selling_post.save()
        print('*********** selling post ', selling_post)
        # serializer = self.serializer_class(data=selling_post)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # print('serializer data ', serializer.data)
        return Response(selling_post, status=status.HTTP_201_CREATED)

