from django.contrib.auth.models import User
from kanvas_app.permissions import CoursePermission
from kanvas_app.models import Course
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CourseDetailSerializer, CourseSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from ipdb import set_trace
    
class CourseView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [CoursePermission]
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        validated_data = serializer.validated_data
        
        course = Course.objects.get_or_create(**validated_data)[0]

        self.check_object_permissions(request, course)     
                 
        serializer = CourseSerializer(course)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CourseDetailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [CoursePermission]

    def put(self, request, course_id):
        serializer = CourseSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        course = Course.objects.filter(id=course_id).first()

        self.check_object_permissions(request, course)  

        if course == None:
            return Response({"errors": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)

        user_ids = request.data.pop('user_ids')

        for user_id in user_ids:
            user = User.objects.filter(id=user_id).first()
            if not user:
                return Response({"errors": "invalid user_id list"}, status=status.HTTP_404_NOT_FOUND)
            if user.is_staff == True or user.is_superuser == True:
                return Response({"errors": "Only students can be enrolled in the course."}, status=status.HTTP_400_BAD_REQUEST)

        course.users.set(user_ids)

        serializer = CourseDetailSerializer(course)
        
        return Response(serializer.data)
    
