# Generated by Django 5.1.4 on 2024-12-10 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rooms', models.ManyToManyField(to='lunchroom_app.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='patron',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lunchroom_app.user'),
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunchroom_app.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunchroom_app.user')),
            ],
        ),
    ]
