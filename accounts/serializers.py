from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"], acceptTerms=validated_data["acceptTerms"],
            bio=validated_data["bio"],
            birthdate=validated_data["birthdate"],
            email=validated_data["email"],
            newsletter=validated_data["newsletter"],
            phone_number=validated_data["phone_number"],
            password=validated_data["password"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ["pk", "username", "password", "acceptTerms", "bio",
                "birthdate", "email", "newsletter", "phone_number"]
