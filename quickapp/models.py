from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)  # ✅ Make sure 'name' is defined
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    fee = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title
    
class UserEventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f"{self.user.username} registered for {self.event.title}"

      