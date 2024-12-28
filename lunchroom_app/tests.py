from django.test import TestCase

from . import models


class TestRoomModel(TestCase):
    def test_user_inherited_from_foods(self):
        patron = models.User.objects.create(name="patron")
        room = models.Room.objects.create(patron=patron)
        assert len(room.users) == 0, "Room should not find any users"

        name = "John"
        user = models.User.objects.create(name=name)
        food_item = models.FoodItem.objects.create(user=user, name="food_1", price=1)
        room.foods.add(food_item)
        assert len(room.users) == 1, "Room should find one user"

        name = "Peter"
        user = models.User.objects.create(name=name)
        food_item = models.FoodItem.objects.create(user=user, name="food_2", price=1)
        room.foods.add(food_item)
        assert len(room.users) == 2, "Room should find two users"
