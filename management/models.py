from django.db import models

# Create your models here.
from django.db import models

class Member(models.Model):
    memid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    zipcode = models.IntegerField()
    telephone = models.CharField(max_length=20)
    # The self-referential recommendation link
    recommendedby = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    joindate = models.DateTimeField()

    def __str__(self):
        return f"{self.firstname} {self.surname}"

class Facility(models.Model):
    facid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    membercost = models.DecimalField(max_digits=10, decimal_places=2)
    guestcost = models.DecimalField(max_digits=10, decimal_places=2)
    initialoutlay = models.DecimalField(max_digits=10, decimal_places=2)
    monthlymaintenance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    facid = models.ForeignKey(Facility, on_delete=models.CASCADE)
    memid = models.ForeignKey(Member, on_delete=models.CASCADE)
    starttime = models.DateTimeField()
    slots = models.IntegerField()