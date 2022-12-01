from django.db import models
from django.contrib.auth.models import User
from sklearn.preprocessing import maxabs_scale
from PIL import Image


# Create your models here.
#class User(models.Model):
#    account = models.CharField(max_length=50)
#    password = models.CharField(max_length=50)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='main/media')
    #bio = models.TextField(null=True, blank=True)
    #telegram = models.CharField(max_length=50, null=True, blank=True)
    #instagram = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        #return f'{self.user.username} Profile'
        return str(self.user)


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
