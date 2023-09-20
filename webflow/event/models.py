from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.


class events(models.Model):
    name = models.CharField(("Event Name"), max_length=250)
    category = models.ForeignKey("event_category", verbose_name=("Category"), on_delete=models.CASCADE)
    start_date_time = models.DateTimeField(("start Date and Time"), auto_now=False, auto_now_add=False)
    end_date_time = models.DateTimeField(("End Date and Time"), auto_now=False, auto_now_add=False)
    center = models.CharField(("Center/organization Name"), max_length=250)
    location = models.CharField(("Location"), max_length=250)
    calender = models.URLField(("Add to Calender link"), max_length=25000)
    about = RichTextField(("About 1"))
    card = models.ImageField(("card 285*150"), upload_to="event/card")
    banner = models.ImageField(("Banner 475*350"), upload_to='event/banner')
    poster = models.ImageField(("Poster"), upload_to='event.poster')
    about2 = RichTextField(("About 2"))   

    entry = models.CharField(("Entry Fee"), max_length=50) 
    organizer = models.ForeignKey("authentication.profiles", verbose_name=("Organizer"), on_delete=models.CASCADE)
    phone = models.CharField(("Main Phone Number"), max_length=50)

    map = models.URLField(("Google link"), max_length=25000)

    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class event_category(models.Model):
    name = models.CharField(("Name"), max_length=50)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    

class adv(models.Model):
    name = models.CharField(("Name"), max_length=50)
    image = models.ImageField(("Adv Image"), upload_to='advertisement/image')

    def __str__(self):
        return self.name
    



class event_registration(models.Model):
    name = models.ForeignKey("authentication.profiles", verbose_name=("Profile - User"), on_delete=models.CASCADE)
    event = models.ForeignKey("events", verbose_name=("Event"),related_name="event", on_delete=models.CASCADE)
    team = models.CharField(("Team"), max_length=50)
    college = models.CharField(("College Name"), max_length=250)
    semester = models.CharField(("Semester"), max_length=50)

    def __str__(self):
        return f"{self.name}"
    