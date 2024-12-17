from django.db import models
import uuid


# Create your models here.
class Busstop(models.Model):
    stopname = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    stop_id = models.CharField(max_length=20, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.stop_id:
            # Generate a unique stop_id if not already set
            self.stop_id = str(uuid.uuid4())[:8]  # Use first 8 characters of UUID
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.stopname
    
class Route(models.Model):
    first_stop = models.ForeignKey(Busstop, related_name='first_stops', on_delete=models.CASCADE)
    last_stop = models.ForeignKey(Busstop, related_name='last_stops', on_delete=models.CASCADE)
    fare_matrix = models.JSONField() 
    route_id = models.CharField(max_length=20, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.stop_id:
            # Generate a unique stop_id if not already set
            self.stop_id = str(uuid.uuid4())[:8]  # Use first 8 characters of UUID
        super().save(*args, **kwargs)


class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    reg_no = models.CharField(max_length=20)
    route_trip1 = models.ForeignKey(Route,related_name='route_trip1', on_delete=models.CASCADE)
    route_trip2 = models.ForeignKey(Route,related_name='route_trip2', on_delete=models.CASCADE)
    route_trip3 = models.ForeignKey(Route,related_name='route_trip3', on_delete=models.CASCADE)