from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Carousel,Feature,Addition,Service,Testimonial,Doctor,Gallery,Price,Faq,Department,Contact
from .form import AppointmentForm,ContactForm
from django.contrib import messages
# Create your views here.



def index(request):

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('/')
        else:
            messages.error(request, 'There was an error with your form. Please try again.')

    else:
        form = ContactForm()
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
    context = {
        "carousels" : carousels,
        "features" : features,
        "additions" : additions,
        "services" : services,
        "testimonials" : testimonials,
        "doctors" : doctors,
        "gallerys" : gallerys,
        "prices" : prices,
        "faqs" : faqs,
        "departments" : departments,
        "form": form,
    }
    
    return render(request, 'index.html', context)

# cantact form visible in database

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


# def logout_view(request):
#     logout(request)
#     return redirect('index') 


# def user_registration(request):
#     form = RegistrationForm()
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             messages.success(request,'You have signed up successfully.')
#             login(request,user)
#             return redirect('/')
#         return render(request, 'registration_form.html', {'form':form})
    



