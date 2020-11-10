from rest_framework import serializers

from ateliersoude.user.models import (
    CustomUser,
)


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
          "first_name",
          "last_name",
          "street_address",
          "email"
        ]
