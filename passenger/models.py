from django.db import models
from django.contrib.auth.models import User
from bus.models import Busstop

# Create your models here.

class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='passenger')

    def __str__(self):
        return self.user.username
    
class Trips(models.Model):
    travelled_by = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='travelled_by')
    entry_point = models.ForeignKey(Busstop, on_delete=models.CASCADE, related_name='entry_point')
    leave_point = models.ForeignKey(Busstop, on_delete=models.CASCADE, related_name='leave_point')
    fare = models.IntegerField()

    def __str__(self):
        return f'{self.entry_point} - {self.leave_point}'
