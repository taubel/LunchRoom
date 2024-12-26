from django.db import models
from django.urls import reverse


# Model representing a 'Room'
#  Room: a congregation of engineers ready to order some food
class Room(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    # TODO decide what to put in 'on_delete'
    patron = models.ForeignKey("User", on_delete=models.PROTECT)
    users = models.ManyToManyField("User", related_name="room_users")

    def get_absolute_url(self):
        return reverse("room-get", kwargs={"pk": self.pk})


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
