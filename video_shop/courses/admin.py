from django.contrib import admin
from .models import Course

# Регістрація таблиці Course в адмін-панелі
admin.site.register(Course)
