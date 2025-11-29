from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import (RegisterView, UserProfileListAPIView, UserProfileDetailAPIView, CategoryListAPIView,
                    SubCategoryViewSet, CourseListAPIView, CourseDetailAPIView, LessonListAPIView,
                    LessonDetailAPIView, AssignmentListAPIView, AssignmentDetailAPIView, OptionListAPIView,
                    QuestionViewSet, ExamListAPIView, ExamDetailAPIView, CertificateViewSet, ReviewCreateAPIView,
                    ReviewEditAPIView)

router = SimpleRouter()
router.register(r'sub_category', SubCategoryViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'certificate', CertificateViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_detail'),
    path('assignment/', AssignmentListAPIView.as_view(), name='assignment_list'),
    path('assignment/<int:pk>/', AssignmentDetailAPIView.as_view(), name='assignment_detail'),
    path('option/', OptionListAPIView.as_view(), name='option_list'),
    path('exam/', ExamListAPIView.as_view(), name='exam_list'),
    path('exam/<int:pk>/', ExamDetailAPIView.as_view(), name='exam_detail'),
    path('review/create/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('review/create/<int:pk>/', ReviewEditAPIView.as_view(), name='review_edit')
]
