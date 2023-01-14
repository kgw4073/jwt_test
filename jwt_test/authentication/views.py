from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import json, re
from .serializers import LoginSerializer, RegistrationSerializer, UserSerializer
from .renderers import UserJSONRenderer
from .models import User

class RegistrationAPIView(APIView):
    permission_classes = (AllowAny, )
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data#.get('user', {})

        serializer = self.serializer_class(data=user)
        print('serializer ', serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print('serializer data ', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class ListView(APIView):
    permission_classes = (AllowAny, )
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def get(self, req):
        users = User.objects.all()
        print('\n\n\n\n\n\nuser get ', users)
        return Response(users, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data
        print('request user ', request.user)
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostView(APIView):
    def post(self, request):
        email = request.user
        exist_user_info = User.objects.filter(email=email).values()
        user_info_dict = list(exist_user_info)[0]
        try:
            new_email = user_info_dict['email']
            new_password = user_info_dict['password']
        except KeyError:
            return Response({'message': "key_error"}, status=400)


            # password validation
        if not len(new_password) >= 8:
            return Response({'message': "invalid password"}, status=400)
        return Response({'message' : "Valid post response"})