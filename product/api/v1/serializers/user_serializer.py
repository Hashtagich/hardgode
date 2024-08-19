from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from users.models import Subscription

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователей."""

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'email', 'balance', 'groups']


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор подписки."""

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'course', 'group']
