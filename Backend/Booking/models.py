from django.db import models
class Booking(models.Model):
    client_name=models.CharField(max_length=200)
    trek_route=models.CharField(max_length=200)
    start_date=models.DateField()
    no_of_people=models.PositiveBigIntegerField()
    deposite=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.client_name} - {self.trek_route} - ({self.start_date}) "
    


