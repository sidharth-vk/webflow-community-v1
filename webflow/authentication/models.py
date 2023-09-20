from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import random

# Create your models here.


DEFAULT_IMAGES = ['image/profile_icon/1.jpg','image/profile_icon/2.jpg','image/profile_icon/3.jpg','image/profile_icon/4.jpg','image/profile_icon/5.jpg','image/profile_icon/6.jpg']

def get_random_default_image():
    return random.choice(DEFAULT_IMAGES)

class skills(models.Model):
    tech = models.CharField(("Technology"), max_length=250)
    image = models.ImageField(("Logo "), upload_to='user/skill')

    def __str__(self):
        return self.tech
    


class profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(("Full Name"), max_length=50)
    about = models.TextField(("About"))
    designation = models.CharField(("Designation"), max_length=50)
    joined = models.CharField(("Date Joined"), max_length=50)
    birthplace = models.CharField(("Birth Place"), max_length=250)
    email = models.CharField(("Email"), max_length=250)
    linkedin = models.CharField(("Linkedin"), max_length=50)
    instagram = models.CharField(("Instagram"), max_length=50)
    github = models.CharField(("Github"), max_length=50)
    dob = models.CharField(("DOB"), max_length=50)
    gender = models.CharField(("Gender"), max_length=50)
    phono = models.CharField(("Phone Number"), max_length=50)
    price = models.CharField(("Freelancers Price / Hour"), max_length=50)
    image = models.ImageField(("Profile Photo"), upload_to='profile/image',default=get_random_default_image)

    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user}'
    

class user_skills(models.Model):
    name = models.ForeignKey("profiles", verbose_name=("Profile - User"), on_delete=models.CASCADE)
    skill = models.ForeignKey("skills", verbose_name=("Skill"),related_name='skill', on_delete=models.CASCADE)

    

class user_work(models.Model):
    name = models.ForeignKey("profiles", verbose_name=("Profile - User"), on_delete=models.CASCADE)
    year = models.CharField(("Year "), max_length=250)
    title = models.CharField(("Title"), max_length=250)
    company = models.CharField(("Company/organisation"), max_length=250)
    des = models.TextField(("Short Description"))

class user_talsk_about(models.Model):
    name = models.ForeignKey("profiles", verbose_name=("Profile - User"), on_delete=models.CASCADE)
    title = models.CharField(("Talks About"), max_length=50)

class user_portfolio(models.Model):
    name = models.ForeignKey("profiles", verbose_name=("Profile - User"), on_delete=models.CASCADE)
    year = models.CharField(("Year "), max_length=250)
    title = models.CharField(("Title"), max_length=250)
    company = models.CharField(("Company/organisation"), max_length=250)
    des = models.TextField(("Short Description"))
    link = models.URLField(("Project Link"))

class user_education(models.Model):
    name = models.ForeignKey("profiles", verbose_name=("Profile - User"), on_delete=models.CASCADE)
    course = models.CharField(("Course"), max_length=250)
    college = models.CharField(("College, Location"), max_length=450)
    start_year = models.CharField(("Start Year "), max_length=250)
    end_year = models.CharField(("end Year "), max_length=250)

class user_follow(models.Model):
    follower = models.ForeignKey("profiles", verbose_name=("follower"),related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey("profiles", verbose_name=("following"),related_name='follower', on_delete=models.CASCADE)


    def __str__(self):
        return f'follower - {self.follower} : following - {self.following} '
    

class core_team(models.Model):
    name = models.ForeignKey("profiles", verbose_name=("Name"), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
    



class profile_rating(models.Model):
    user = models.ForeignKey("profiles", verbose_name=("Name"), on_delete=models.CASCADE)
    name = models.CharField(("Name"), max_length=250)
    email = models.CharField(("Email"), max_length=250)
    comment = RichTextField()
    rating = models.IntegerField(("Rating"))

    def __str__(self):
        return self.name 
    

class origaniser(models.Model):
    user = models.ForeignKey("profiles", verbose_name=("Name"), on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user}"
    
