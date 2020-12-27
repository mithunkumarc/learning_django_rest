from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.
class Event(models.Model):
    class StateChoice(models.TextChoices):
        Alabama = 'Alabama, AL'
        Arizona = 'Arizona, AR'
        Wyoming = 'Wyoming, WY'

    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(
        max_length=50, choices = StateChoice.choices, default = StateChoice.Alabama
    )
    zipcode = models.CharField(max_length=10)
    other = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    category = models.CharField(max_length=25)
    list_date = models.DateTimeField(default=now, blank=True)

    class Meta:
        verbose_name_plural = 'events'

    def __str___(self):
        return self.title
