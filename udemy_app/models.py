from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField



class UserProfile(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    phone_number = PhoneNumberField()
    RoleChoices = (
    ('client', 'client'),
    ('teacher', 'teacher'),
    )
    role = models.CharField(max_length=30, choices=RoleChoices, default='client')
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_picture', null=True, blank=True)


    def __str__(self):
        return self.username



class Category(models.Model):
    category_name = models.TextField()

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name

class Course(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)
    description = models.TextField()
    LevelChoices = (
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
    )
    level = models.CharField(max_length=25, choices=LevelChoices, default='Beginner')
    price = models.PositiveIntegerField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name

class Lesson(models.Model):
    tittle = models.CharField(max_length=50)
    video_url = models.FileField(upload_to='lesson_video/')
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.tittle

class Assignment(models.Model):
    tittle = models.CharField(max_length=70)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.tittle


class Option(models.Model):
    option_name = models.CharField(max_length=80)
    type_option = models.BooleanField(null=True)


    def __str__(self):
        return self.option_name

class Question(models.Model):
    questions_name = models.CharField(max_length=90, null=True, blank=True)
    questions_text = models.TextField()
    option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.questions_name


class Exam(models.Model):
    tittle = models.CharField(max_length=70)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    duration = models.DurationField()

    def __str__(self):
        return self.tittle

class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_url = models.FileField(upload_to='certificate')

class Review(models.Model):
    user_review = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()

