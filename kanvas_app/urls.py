from kanvas_app.models import Submission
from django.urls import path
from .views import ActivityDetailView, ActivityView, CourseDetailView, CourseView, SubmissionView

urlpatterns = [
    path('courses/', CourseView.as_view()),
    path('courses/<int:course_id>/registrations/', CourseDetailView.as_view()),
    path('courses/<int:course_id>/', CourseDetailView.as_view()),
    path('activities/', ActivityView.as_view()),
    path('activities/<int:activity_id>/submissions/', ActivityDetailView.as_view()),
    path('submissions/<int:submission_id>/', SubmissionView.as_view()),
    path('submissions/', SubmissionView.as_view())
]