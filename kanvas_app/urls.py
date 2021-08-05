from django.urls import path
from .views import CourseDetailView, CourseView

urlpatterns = [
    path('courses/', CourseView.as_view()),
    path('courses/<int:course_id>/registrations/', CourseDetailView.as_view())
]