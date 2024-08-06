from rest_framework.serializers import ModelSerializer
from dashboard import models as dash_models
from users import models as user_models

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = dash_models.Services
        fields = '__all__'


class StaffSerializer(ModelSerializer):
    class Meta:
        model = dash_models.Staff
        fields = '__all__'


class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = dash_models.Portfolio
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = user_models.User
        fields = ['pk', 'username', 'first_name', 'last_name', 'password']


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = user_models.Review
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model = user_models.Contact
        fields = '__all__'




