from django.db import models
from django.utils.text import slugify

# Create your models here.
class group(models.Model):
    name = models.CharField(("Title"), max_length=250)
    about = models.TextField(("About"))
    formed = models.CharField(("Group Formed"), max_length=50)
    img = models.ImageField(("Card Image"), upload_to='group/card')
    img2 = models.ImageField(("banner Image"), upload_to='group/banner')
    leader = models.ForeignKey("authentication.profiles", verbose_name=("Leader"), on_delete=models.CASCADE)

    price = models.CharField(("Price For hire/Hour"), max_length=50)
    email = models.CharField(("Email"), max_length=50)
    phone = models.CharField(("Phone Number"), max_length=50)
    priority = models.IntegerField(("priority"))

    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class grp_member(models.Model):
    group = models.ForeignKey("group", verbose_name=("Group"), on_delete=models.CASCADE)
    user = models.ForeignKey("authentication.profiles", verbose_name=("Name"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group} - {self.user}"
    


class grp_feed(models.Model):
    author = models.ForeignKey("authentication.profiles", verbose_name=("Author"),related_name='author', on_delete=models.CASCADE)
    date = models.CharField(("Date"), max_length=50)
    group = models.ForeignKey("group", verbose_name=("Group"),related_name='group', on_delete=models.CASCADE)
    img = models.ImageField(("Image 660*450"), upload_to='group/feed')
    link = models.CharField(("Link"), max_length=12350)

    
    
class grp_skills(models.Model):
    group = models.ForeignKey("group", verbose_name=("Group"), on_delete=models.CASCADE)
    tech = models.CharField(("Technology"), max_length=250)
    image = models.ImageField(("Logo "), upload_to='user/skill')



class grp_talks_about(models.Model):
    group = models.ForeignKey("group", verbose_name=("Group"), on_delete=models.CASCADE)
    title = models.CharField(("Talks About"), max_length=50)

