from rest_framework import serializers

from members.models import User
from utils import hash256


class LoginForm(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        return User.login(validated_data['password'],
                          validated_data['username'])


class RegisterForm(serializers.Serializer):
    nick_name = serializers.CharField()
    password = serializers.CharField()

    def validate_nick_name(self, value):
        if User.objects.filter(nick_name=value).exists():
            raise serializers.ValidationError('该用户名已存在')

        return value

    def validate_password(self, value):
        return hash256(value)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
