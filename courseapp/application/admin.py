from django.contrib import admin

from .models import Category, Comment, Tag, Lesson, Course, Rating

# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(Rating)
