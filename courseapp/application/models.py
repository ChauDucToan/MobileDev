from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=True)
    category_id = models.ForeignKey(Category, on_delete=models.RESTRICT)

class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='application/%Y/%m')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

class LessonTags(models.Model):
    lesson_id = models.ForeignKey(Lesson, on_delete=models.RESTRICT)
    tag_id = models.ForeignKey(Tag, on_delete=models.RESTRICT)

class Comment(BaseModel):
    content = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT)

class Rating(BaseModel):
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    lesson_id = models.ForeignKey(Lesson, on_delete=models.RESTRICT)
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT)
