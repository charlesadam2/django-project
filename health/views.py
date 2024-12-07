from django.shortcuts import render
from .models import Carousel,Feature,Addition,Service,Testimonial,Doctor,Gallery,Price,Faq,Department

# Create your views here.


def index(request):
    carousels = Carousel.objects.all()
    features = Feature.objects.all()
    additions = Addition.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    doctors = Doctor.objects.all()
    gallerys = Gallery.objects.all()
    prices = Price.objects.all()
    faqs = Faq.objects.all()
    departments = Department.objects.all()
    return render(request, 'index.html')

