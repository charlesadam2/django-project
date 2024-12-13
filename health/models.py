from django.db import models

# Create your models here.

class Carousel(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
class Feature(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    icon = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
    

class Addition(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True,null=True)
    icon = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
    

class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    icon = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    content = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
    

class Doctor(models.Model):
    image = models.ImageField(upload_to='images/')
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    image = models.ImageField(upload_to='images/')


class Price(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    features = models.JSONField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField(blank=True,null=True)


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    email = models.EmailField()
    full_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.full_name
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
    
    



    
