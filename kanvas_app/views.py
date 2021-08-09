from re import sub
from django.contrib.auth.models import User
import ipdb
from rest_framework.fields import NullBooleanField
from kanvas_app.permissions import CoursePermission, CourseStudentPermission, CourseSuperUserPermission
from kanvas_app.models import Activity, Course, Submission
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ActivitySerializer, CourseDetailSerializer, CourseSerializer, SubmissionDetailSerializer, SubmissionSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from ipdb import set_trace
    
class CourseView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [CourseSuperUserPermission]
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        validated_data = serializer.validated_data
        
        course = Course.objects.get_or_create(**validated_data)[0]

        self.check_object_permissions(request, course)     
                 
        serializer = CourseSerializer(course)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):    
        course = Course.objects.all()
        
        serialized = CourseDetailSerializer(course, many=True)
        return Response(serialized.data)

class CourseDetailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [CourseSuperUserPermission]

    def put(self, request, course_id):
        serializer = CourseSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        course = Course.objects.filter(id=course_id).first()

        self.check_object_permissions(request, course)  

        if course == None:
            return Response({"errors": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)

        user_ids = request.data.pop('user_ids')

        if type(user_ids) is not list:
            return Response({"errors": "invalid user_id list"}, status=status.HTTP_400_BAD_REQUEST)

        for user_id in user_ids:
            user = User.objects.filter(id=user_id).first()
            
            if not user :
                return Response({"errors": "invalid user_id list"}, status=status.HTTP_404_NOT_FOUND)
        
        for user_id in user_ids:
            user = User.objects.filter(id=user_id).first()
            
            if user.is_staff == True or user.is_superuser == True:
                return Response({"errors": "Only students can be enrolled in the course."}, status=status.HTTP_400_BAD_REQUEST)
        course.users.set(user_ids)

        serializer = CourseDetailSerializer(course)
        
        return Response(serializer.data)
    
    def get(self, request, course_id=''):

        course = Course.objects.filter(id=course_id).first()

        if course == None:
            return Response({"errors": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseDetailSerializer(course)
        return Response(serializer.data)

    def delete(self, request, course_id):

        course = Course.objects.filter(id=course_id).first()

        self.check_object_permissions(request, course)  

        if course == None:
            return Response({"errors": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)
        
        course.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ActivityView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [CoursePermission]

    def post(self, request):
        serializer = ActivitySerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        validated_data = serializer.validated_data

        activity1 = Activity.objects.filter(title=request.data["title"]).first()

        activity2 = Activity.objects.filter(title=request.data["title"])

        if activity1 != None:

            self.check_object_permissions(request, activity1)   

            activity2.update(**serializer.validated_data)  
                    
            serializer = ActivitySerializer(activity2.first())

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            activity = Activity.objects.get_or_create(**validated_data)[0]

            self.check_object_permissions(request, activity)     
                    
            serializer = ActivitySerializer(activity)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):    
        activities = Activity.objects.all()

        self.check_object_permissions(request, activities)  

        serialized = ActivitySerializer(activities, many=True)

        return Response(serialized.data)

class ActivityDetailView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [CourseStudentPermission]

    def post(self, request, activity_id=''):

        serializer = SubmissionSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        validated_data = serializer.validated_data

        submission = Submission.objects.create(grade=None, repo=serializer["repo"].value, user=request.user, activity=Activity.objects.filter(id=activity_id).first())

        self.check_object_permissions(request, submission)   

        serializer = SubmissionSerializer(submission)
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    
    
class SubmissionView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [CoursePermission]

    def put(self, request, submission_id):
        serializer = SubmissionSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        submission = Submission.objects.filter(id=submission_id)

        self.check_object_permissions(request, submission)  

        if submission == None:
            return Response({"errors": "invalid submission_id"}, status=status.HTTP_404_NOT_FOUND)

        submission.update(**serializer.validated_data)

        sub = submission.first()

        serializer = SubmissionSerializer(sub)

        return Response(serializer.data)
    
    def get(self, request):    

        if request.user.is_superuser == False and request.user.is_staff == False:

            submissions = Submission.objects.filter(user_id=request.user.id)
            
            serialized = SubmissionSerializer(submissions, many=True)

            return Response(serialized.data)

        else:

            submissions = Submission.objects.all()
            
            serialized = SubmissionSerializer(submissions, many=True)

            return Response(serialized.data)