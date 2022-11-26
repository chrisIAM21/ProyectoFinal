from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    # image = models.ImageField(upload_to='about_us/')

    class Meta:
        verbose_name = 'Historia'
        verbose_name_plural = 'Historia'

    def __str__(self):
        return self.title


class Why_Choose_Us(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name = 'Virtud'
        verbose_name_plural = 'Virtudes'

    def __str__(self):
        return self.title


class Chef(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField(upload_to='chef/')    

    class Meta:
        verbose_name = 'staff'
        verbose_name_plural = 'staff'

    def __str__(self):
        return self.name