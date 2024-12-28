from django import forms

from . import models


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = models.FoodItem
        fields = ["name", "price", "room", "user"]

    def save(self, commit: bool=True):
        food_item = super().save(commit=commit)

        if commit:
            room = models.Room.objects.get(pk=food_item.room.id)
            room.foods.add(food_item)

        return food_item
