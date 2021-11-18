from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.utils.text import slugify

import datetime

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,max_length=500, verbose_name=_("User") , on_delete=models.CASCADE)
    slug = models.SlugField(blank=True , null=True)
    image = models.ImageField(upload_to='profile_img' ,verbose_name=_("Image") ,blank=True, null=True )
    country = CountryField(blank=True , null=True)
    address = models.CharField(max_length=500 , blank=True , null=True)
    join_date = models.DateTimeField(verbose_name=_("Join Date"),default=datetime.datetime.now() )
    
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile,self).save(*args, **kwargs)
        

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"slug": self.pk})
    
    def __str__(self):
        return '%s' %self.user

def create_profile(sender , **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile,sender=User)