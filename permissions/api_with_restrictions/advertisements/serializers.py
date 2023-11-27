from django.contrib.auth.models import User
from django.forms import ValidationError
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = '__all__'

    def create(self, validated_data):
        """Метод для создания"""

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        if self.context['request'].method == 'POST':
            creator = self.context['request'].user
            valid_statuses = Advertisement.objects.filter(creator=creator, status='OPEN')

            if len(valid_statuses) > 10:
                raise ValidationError('Превышено число открытых объявлений')

        return data
