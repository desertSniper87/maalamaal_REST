from django.contrib.auth.models import User, Group
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data

        user = User.objects.get(username=data.get('username'))
        token = Token.objects.create(user=user)
        print(f'token.key: {token.key}')
        data['token'] = str(token)

        group = user.groups.first()
        data['account_type'] = group.name

        headers = self.get_success_headers(data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(http_method_names=['POST'])
def login(request):
    user = User.objects.get(username=request.data.get('username'))
    token_key = Token.objects.get(user=user).key
    return Response({
        'username': user.username,
        'token': token_key
    })

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer





