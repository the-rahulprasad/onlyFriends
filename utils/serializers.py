from rest_framework import serializers
from utils.models import Post, Homie
from django.contrib.auth.models import User

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'

class HomieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homie
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostFullDetailSerializer(serializers.ModelSerializer):
    author = HomieSerializer()
    class Meta:
        model = Post
        fields = '__all__'


