from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.template.context_processors import static
from django.template.context_processors import media
from django.conf import settings
from django.views.generic.dates import timezone_today



class Tag(models.Model):
    # memorial = models.ForeignKey('Memorial', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
   # memorials = models.ManyToManyField('Memorial', related_name='tagged_by')

    def __str__(self):
        return f"{self.name}"

class Memorial(models.Model):
    memorialid = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dateofbirth = models.DateField()
    dateofdeath = models.DateField()
    biography = models.TextField()
    tags =models.ManyToManyField('Tag', related_name='memorial_tags')
    image = models.ImageField(null=True, blank=True, upload_to='images/')


    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def get_absolute_url(self):
        return reverse("Memorialdetail", kwargs={"pk": self.pk})




class Photo(models.Model):
    photoid = models.AutoField(primary_key=True)

    image = models.ImageField(null=True, blank=True, upload_to='photos/')
    datepost = models.DateTimeField(default=timezone.now)
    memorial = models.ForeignKey('Memorial', on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return str(self.image)


class Message(models.Model):
    messageid = models.AutoField(primary_key=True)
    memorial = models.ForeignKey(Memorial, related_name='messages',on_delete= models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
    content = models.TextField()
    dateposted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s  %s - %s' % (self.memorial.firstname, self.memorial.lastname, self.user)



