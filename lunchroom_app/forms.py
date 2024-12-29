from django import forms

from . import models


class FoodItemForm(forms.ModelForm):
    room = forms.ModelChoiceField(models.Room.objects)

    class Meta:
        model = models.FoodItem
        fields = ["name", "price", "user"]

    def save(self, commit: bool=True):
        food_item = super().save(commit=commit)

        if commit:
            room_id = self.cleaned_data["room"].id
            room = models.Room.objects.get(pk=room_id)
            room.foods.add(food_item)

        return food_item
