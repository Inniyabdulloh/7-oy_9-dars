from rest_framework import status
from rest_framework.decorators import api_view
from dashboard.decorator import is_staff
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from users import models as user_models
from dashboard import models as dashboard_models
# Create your views here.



class UserView(APIView):
    def get(self, request, *args, **kwargs):
        users = user_models.User.objects.get(pk=kwargs['pk'])
        serializer = serializers.UserSerializer(users)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @is_staff
    def patch(self, request, *args, **kwargs):
        try:
            user = user_models.User.objects.get(pk=kwargs['pk'])
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @is_staff
    def delete(self, request, *args, **kwargs):
        try:
            user_models.User.objects.get(pk=kwargs['pk']).delete()
            return Response(data={'detail: User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(data={'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST )



class PortfolioView(APIView):
    def get(self, request, *args, **kwargs):
        portfolio = dashboard_models.Portfolio.objects.all()
        serializer = serializers.PortfolioSerializer(portfolio, many=True)
        return Response(serializer.data)

    # @is_staff
    def post(self, request, *args, **kwargs):
        serializer = serializers.PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @is_staff
    def patch(self, request, *args, **kwargs):
        try:
            portfolio = dashboard_models.Portfolio.objects.get(pk=kwargs['pk'])
        except :
            return Response(data={'detail: Portfolio not fouund'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.PortfolioSerializer(portfolio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @is_staff
    def delete(self, request, *args, **kwargs):
        try:
            dashboard_models.Portfolio.objects.get(pk=kwargs['pk']).delete()
            return Response(data={'detail: Portfolio deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(data={'detail': 'Portfolio does not exist'}, status=status.HTTP_400_BAD_REQUEST )



class ServiseView(APIView):
    def get(self, request, *args, **kwargs):
        servise = dashboard_models.Services.objects.all()
        serializer = serializers.PortfolioSerializer(servise, many=True)
        return Response(serializer.data)

    # @is_staff
    def post(self, request, *args, **kwargs):
        serializer = serializers.ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @is_staff
    def patch(self, request, *args, **kwargs):
        try:
            servise = dashboard_models.Services.objects.get(pk=kwargs['pk'])
        except :
            return Response(data={'detail: Portfolio not fouund'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.PortfolioSerializer(servise, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @is_staff
    def delete(self, request, *args, **kwargs):
        try:
            dashboard_models.Services.objects.get(pk=kwargs['pk']).delete()
            return Response(data={'detail: Servise deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(data={'detail': 'Servise does not exist'}, status=status.HTTP_400_BAD_REQUEST )



class StaffView(APIView):
    def get(self, request, *args, **kwargs):
        staff = dashboard_models.Staff.objects.all()
        serializer = serializers.StaffSerializer(staff, many=True)
        return Response(serializer.data)

    # @is_staff
    def post(self, request, *args, **kwargs):
        serializer = serializers.StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @is_staff
    def patch(self, request, *args, **kwargs):
        try:
            staff = dashboard_models.Staff.objects.get(pk=kwargs['pk'])
        except :
            return Response(data={'detail: Staff not fouund'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.StaffSerializer(staff, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @is_staff
    def delete(self, request, *args, **kwargs):
        try:
            dashboard_models.Staff.objects.get(pk=kwargs['pk']).delete()
            return Response(data={'detail: Staff deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(data={'detail': 'Staff does not exist'}, status=status.HTTP_400_BAD_REQUEST )



class ReviewView(APIView):
    def get(self, request, *args, **kwargs):
        review = user_models.Review.objects.all()
        serializer = serializers.ReviewSerializer(review, many=True)
        return Response(serializer.data)

    # @is_staff
    def post(self, request, *args, **kwargs):
        serializer = serializers.ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @is_staff
    def patch(self, request, *args, **kwargs):
        try:
            review = user_models.Review.objects.get(pk=kwargs['pk'])
        except :
            return Response(data={'detail: Review not fouund'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @is_staff
    def delete(self, request, *args, **kwargs):
        try:
            user_models.Review.objects.get(pk=kwargs['pk']).delete()
            return Response(data={'detail: Review deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(data={'detail': 'Review does not exist'}, status=status.HTTP_400_BAD_REQUEST )


class ContactView(APIView):
    def get(self, request, *args, **kwargs):
        contact = user_models.Contact.objects.all()
        serializer = serializers.ContactSerializer(contact, many=True)
        return Response(serializer.data)

    # @is_staff
    def post(self, request, *args, **kwargs):
        serializer = serializers.ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @is_staff
    def patch(self, request, *args, **kwargs):
        try:
            contact = user_models.Contact.objects.get(pk=kwargs['pk'])
        except :
            return Response(data={'detail: Contact not fouund'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ContactSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @is_staff
    def delete(self, request, *args, **kwargs):
        try:
            user_models.Contact.objects.get(pk=kwargs['pk']).delete()
            return Response(data={'detail: Contact deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(data={'detail': 'Contact does not exist'}, status=status.HTTP_400_BAD_REQUEST )