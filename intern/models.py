from django.db import models


class Intern(models.Model):
    sender_name=models.CharField( max_length=50 )
    reciver_name=models.CharField( max_length= 100)
    amount=models.IntegerField()

    def __str__(self):
        return self.sender_name
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email=models.EmailField(primary_key=True)
    mobile=models.CharField(max_length=10)


    def __str__(self):
        return self.first_name
