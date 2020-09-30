from django.db import models


class ActivityPeriods(models.Model):
     """ activity_periods """
     start_time = models.DateTimeField()
     end_time   = models.DateTimeField()

    #  def __str__(self):
    #       return super().__str__()

class UserData(models.Model):
    id               = models.CharField(max_length=20, primary_key=True)
    real_name        = models.CharField(max_length=20, null=True)
    tz               = models.CharField(max_length=20, null=True)
    activity_periods = models.ManyToManyField(ActivityPeriods) 
    
    def __str__(self):
            return super().__str__()