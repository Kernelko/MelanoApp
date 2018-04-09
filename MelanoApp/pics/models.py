from django.db import models

#remember makemigrations (sqlmigrate pics 001 if you want to see SQL) and then migrate
# Create your models here.
class Mark(models.Model):
    """single skin mark that will be observed"""
    ref = models.CharField(max_length=250)
    loc= models.CharField(max_length=250)
    
    def __str__(self):
        return self.ref+ ' located: ' + self.loc

class Picture_file(models.Model):
    """single picture with mark"""
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    picture_date= models.DateField()
    #picture = models.ImageField()
    is_cancer = models.BooleanField(default=True)

    def __str__(self):
        return str(self.picture_date)

