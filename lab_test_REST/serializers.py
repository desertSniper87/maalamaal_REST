from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'username', 'email', 'account_type')

    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField( validators=[UniqueValidator(queryset=User.objects.all())])
    account_type = serializers.CharField(write_only=True)
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        print(validated_data)
        try:
            user = User.objects.create(username=validated_data['username'],
                                       email=validated_data['email'],
                                       password=validated_data['password'])
        except AssertionError as a:
            print(a)


        # try:
        user_group = Group.objects.get(name=validated_data['account_type'])
        user.groups.set([user_group])
        user.save()
        # except Not

        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
