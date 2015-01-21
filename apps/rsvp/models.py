from django.db import models


class Person(models.Model):
    """This model holds personal information about an individual. It stores
    the first name, last name, and email address of a person.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, primary_key=True)


class Rsvp(models.Model):
    """This model holds information about an individual's attendance to the
    wedding. This gathers person's name and email address and if attending
    the number of additional guests as well as meal preferences.
    """
    MEAL_CHOICES = [
        ('CHI', 'Chicken'),
        ('VEG', 'Vegetarian')
    ]

    person = models.OneToOneField(Person, primary_key=True)
    attendance = models.BooleanField(default=None)
    guests = models.PositiveSmallIntegerField(default=0)
    meal_preference = models.CharField(max_length=3, choices=MEAL_CHOICES)
