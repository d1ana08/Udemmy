from .models import *
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name', 'username', 'email', 'password',
                  'phone_number', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class SubCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = {'category_name'}

class CourseListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name']

class CourseDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'description', 'level', 'price',
                  'created_at', 'updated_at']

class LessonListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'tittle']

class LessonDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['tittle', 'video_url', 'content']

class AssignmentListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'tittle']

class AssignmentDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['tittle', 'description', 'due_date']

class OptionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'option_name', 'type_option']

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['questions_name', 'questions_text']

class ExamListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'tittle']

class ExamDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['tittle', 'duration']

class CertificateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['issued_at', 'certificate_url']

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['comment', 'rating']