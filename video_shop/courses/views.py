from .models import Course, Lesson
from django.views.generic import ListView, DeleteView
from django.shortcuts import render
from cloudipsp import Api, Checkout
import time

class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Головна сторінка'
        return ctx

def tarrifsPage(request):
    api = Api(merchant_id=1536773,
            secret_key='iGYhDhP064ILgZjzwi33ViMHZzxpHuwL')
    checkout = Checkout(api=api)
    data = {
        "currency": "USD",
        "amount": 1500,
        "order_desc": "Купівля підписки на сайті",
        "order_id": str(time.time())
    }
    url = checkout.url(data).get('checkout_url')
    return render(request, 'courses/tarrifs.html', {'title': 'Тарифи на курси','url': url})
    
    

class CourseDetailPage(DeleteView):
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)
        ctx['title'] = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['lessons'] = Lesson.objects.filter(course=ctx['title']).order_by('number')
        return ctx
    
 
class LessonDetailPage(DeleteView):
    model = Course
    template_name = 'courses/lessons-detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = list(Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).values())
        ctx['title'] = lesson[0]['title']
        ctx['desc'] = lesson[0]['description']
        ctx['video'] = lesson[0]['video_url'].split('=')[1]

        return ctx