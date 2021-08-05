from accounts.serializers import UserDetailSerializer, UserSerializer
from rest_framework import serializers   


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)
    users = UserSerializer(read_only=True, many=True)

class CourseDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)
    users = UserDetailSerializer(read_only=True, many=True)

