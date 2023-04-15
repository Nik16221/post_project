from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from AdPost.models import User, Post, Comment
from AdPost.permissions import IsOwner
from AdPost.serializers import UserSerializers, PostSerializers, CommentSerializers


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_permissions(self):

        if self.action == ['list', 'retrieve']:
            permission_classes = [IsAdminUser | IsAuthenticated]
        elif self.action == ['create']:
            permission_classes = [AllowAny]
        elif self.action == ['delete']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAdminUser, IsOwner]
        return [permission() for permission in permission_classes]


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get_permissions(self):

        if self.action == ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action == ['create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser | IsOwner]
        return [permission() for permission in permission_classes]


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

    def get_permissions(self):

        if self.action == ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action == ['create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser | IsOwner]
        return [permission() for permission in permission_classes]


class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
