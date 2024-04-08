from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from posts.serializers import UserSerializer, GroupSerializer, PostSerializer, BusinessSerializer, CategorySerializer
from posts.models import Post, Business, Category

#api endpoint allow us to create new users, view all users, update a users
class UserViewSet(viewsets.ModelViewSet):
    #grabbing all the objects and order them by the date they joined
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permissions.IsAuthenticated forces users to be logged in to be able to make get/post requests
    permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #allow users who aren't logged in to still view posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    #allow users who aren't logged in to still view businesses
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #allow users who aren't logged in to still view posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]