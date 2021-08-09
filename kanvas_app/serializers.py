from kanvas_app.models import Submission
from accounts.serializers import UserDetailSerializer, UserIdSerializer, UserSerializer
from rest_framework import serializers   


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)
    users = UserSerializer(read_only=True, many=True)

class CourseDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)
    users = UserDetailSerializer(read_only=True, many=True)

class ActivityDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

class SubmissionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    grade = serializers.FloatField(required=False)
    repo = serializers.CharField(required=False)
    user_id = serializers.IntegerField(read_only=True)
    activity_id = serializers.IntegerField(read_only=True)
    

class SubmissionDetailSerializer(serializers.Serializer):
    user = serializers.IntegerField(required=False)
    activity = serializers.IntegerField(required=False)

class ActivitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    points = serializers.IntegerField(required=False)
    submissions = SubmissionSerializer(many=True, required=False)
