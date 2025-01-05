from bs4 import BeautifulSoup
from django.test import TestCase
from django.urls import reverse

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

    def test_fooditem_form_no_initial_room(self):
        response = self.client.get(reverse("food-add"))

        self.assertEqual(response.status_code, 200)

        html = BeautifulSoup(response.content)
        html_select = html.find("select", id="id_room")
        self.assertIsNotNone(html_select)

        html_option = html_select.find("option", value="")
        self.assertIsNotNone(html_option)
        self.assertTrue(html_option.has_attr("selected"))

    # TODO test seems to fail because of no rooms defined in database
    #  Prepare testing database
    def test_fooditem_form_initial_room(self):
        room_id = "5"
        response = self.client.get(reverse("food-add"), query_params={"room_id": room_id})

        self.assertEqual(response.status_code, 200)

        html = BeautifulSoup(response.content)
        html_select = html.find("select", id="id_room")
        self.assertIsNotNone(html_select)

        html_option = html_select.find("option", value=room_id)
        self.assertIsNotNone(html_option)
        self.assertTrue(html_option.has_attr("selected"))
