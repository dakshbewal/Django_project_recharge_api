from django.db import models




# Create your models here.
class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    planId = models.CharField(max_length=50)
    bplInventoryItemId = models.IntegerField()
    billPlanName = models.CharField(max_length=50, default="")
    freebieCount = models.IntegerField(default=0)
    pricePoint = models.IntegerField()
    billPlanCategory = models.CharField(max_length=50)
    planComponents = models.JSONField()

    def __str__(self):
        return self.billPlanName

