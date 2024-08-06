from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from users import models as user_models
from dashboard import models as dashboard_models
# Create your views here.

class UserView(APIView):
    def get(self, request, *args, **kwargs):
        users = user_models.User.objects.get(pk=kwargs['pk'])
        print("salom api")
        serializer = serializers.UserSerializer(users)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        try:
            user = user_models.User.objects.get(pk=kwargs['pk'])
        except user_models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)