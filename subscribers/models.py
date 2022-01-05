from django.db import models

# Create your models here.
class subscribers (models.Model):
    """Subscriber model."""
    email = models.CharField(max_length=100,blank=False, null=False, help_text="email address")
    full_name = models.CharField(max_length=100, blank=False, null=False, help_text="First and LastName")

    def __str__(self):
        """Str repr of this object"""
        return  self.full_name
    class Meta:
        verbose_name ="Subscriber"
        verbose_name_plural = "Subscribers"