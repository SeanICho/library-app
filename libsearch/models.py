from django.db import models

class EventDetails(models.Model):
    change_message = models.CharField(max_length=10, blank=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    group = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    register = models.BooleanField()

    def __str__(self):
        return self.title
