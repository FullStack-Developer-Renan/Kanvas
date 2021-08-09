from rest_framework.permissions import BasePermission
import ipdb

        
class CoursePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user.is_staff
        
class CourseSuperUserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser 

class CourseStudentPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return not request.user.is_superuser and not request.user.is_staff