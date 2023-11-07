from django.contrib import admin
from .models import Course, Lesson

# Регістрація таблиці Course в адмін-панелі
admin.site.register(Course)
admin.site.register(Lesson)

