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
    user = UserIdSerializer(read_only=True)
    activity = ActivityDetailSerializer(read_only=True)
    

class SubmissionDetailSerializer(serializers.Serializer):
    user = serializers.IntegerField(required=False)
    activity = serializers.IntegerField(required=False)

class ActivitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    points = serializers.FloatField()
    submissions = SubmissionSerializer(read_only=True, many=True)


# from rest_framework import serializers
# from collections import OrderedDict

# class SimpleSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     age = serializers.IntegerField(required=True)
    
# class ArtistSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=False)
#     formed_in = serializers.IntegerField(required=False)
#     status = serializers.CharField(required=False)
    
# class SongSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     artist = ArtistSerializer()
    
# class SongSimpleSerializer(serializers.Serializer):    
#     title = serializers.CharField()
    
    
# class ArtistSongsSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     formed_in = serializers.IntegerField()
#     status = serializers.CharField()
#     musics = SongSimpleSerializer(many=True, source='songs')
#     total_songs = serializers.SerializerMethodField()
    
#     def get_total_songs(self, obj):
#         if (isinstance(obj, OrderedDict)):
#             return 0
#         return { 'count': obj.songs.count()}
    
# class PlaylistSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     songs = SongSerializer(many=True)