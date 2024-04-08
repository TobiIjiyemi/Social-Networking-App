from django.contrib.auth.models import User, Group
from rest_framework import serializers
from posts.models import Post, Business, Category

#inheriting from hyperlinkedmodel serializer
#use a hyperlink relation instead of usual primary key relation
#using a URL instead of a primary key

#take the django data, convert to python data (lists, dictionnaries), and convert to json
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'