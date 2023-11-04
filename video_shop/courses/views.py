from .models import Course
from django.views.generic import ListView, DeleteView


class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Головна сторінка'
        return ctx
    

class CourseDetailPage(DeleteView):
    model = Course
    template_name = 'courses/course-detail.html'