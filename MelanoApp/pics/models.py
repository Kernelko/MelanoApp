from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime
#remember makemigrations (sqlmigrate pics 001 if you want to see SQL) and then migrate
# Create your models here.
class Mark(models.Model):
    """single skin mark that will be observed"""
    ref = models.CharField(max_length=250)
    loc= models.CharField(max_length=250)
    current_pic = models.FileField(null=True, blank=True)
    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    picture_date= models.DateField(default=datetime.date.today)
    is_cancer = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('pics:detail', kwargs = {'pk': self.pk})

    def __str__(self):
        return self.ref+ ' located: ' + self.loc

class Picture_file(models.Model):
    """single picture with mark"""
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    picture_date= models.DateField()
    picture_file = models.FileField(null=True, blank=True)
    is_cancer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.picture_date)

