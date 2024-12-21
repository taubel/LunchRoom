from django.db import models
from django.urls import reverse


# Model representing a 'Room'
#  Room: a congregation of engineers ready to order some food
class Room(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    # TODO decide what to put in 'on_delete'
    patron = models.ForeignKey("User", on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse("room-detail", kwargs={"pk": self.pk})


class User(models.Model):
    name = models.CharField(max_length=100)


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
