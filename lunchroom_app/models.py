from django.db import models


# Model representing a 'Room'
#  Room: a congregation of engineers ready to order some food
class Room(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    # TODO decide what to put in 'on_delete'
    patron = models.ForeignKey("User", on_delete=models.PROTECT)


class User(models.Model):
    name = models.CharField(max_length=100)
    rooms = models.ManyToManyField(Room)


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
