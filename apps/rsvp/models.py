from django.db import models
from django.utils.text import slugify


class Person(models.Model):
    """This model holds personal information about an individual. It stores
    the first name, last name, and email address of a person.
    """
    first_name = models.CharField('first name of person',
                                  max_length=50)
    last_name = models.CharField('last name of person',
                                 max_length=50)
    email = models.EmailField('email address submitted for person',
                              max_length=254, primary_key=True)
    slug = models.SlugField('slug to identify person',
                            editable=False,
                            max_length=101)

    class Meta:
        unique_together = (('first_name', 'last_name', 'email'),)

    def save(self, *args, **kwargs):
        self.slug = slugify('{0}'.format(self.email))
        for field_name in ['first_name', 'last_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.strip().capitalize())
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        message = 'email: {0}, last name: {1}, first name {2}'
        return message.format(self.email, self.last_name, self.first_name)


class Rsvp(models.Model):
    """This model holds information about an individual's attendance to the
    wedding. This gathers person's name and email address and if attending
    the number of additional guests as well as meal preferences.
    """
    MEAL_CHOICES = [
        ('CHI', 'Chicken'),
        ('VEG', 'Vegetarian')
    ]
    BOOLEAN_CHOICES = ((True, "Wouldn't miss it for the world."),
                       (False, "Regretfully, cannot make it."))

    person = models.OneToOneField(Person, primary_key=True,
                                  verbose_name='Person associated to Rsvp')
    attendance = models.BooleanField('True if Person is attending',
                                     choices=BOOLEAN_CHOICES,
                                     default=None)
    guests = models.PositiveSmallIntegerField('Number of guests of Person',
                                              default=0)
    meal_preference = models.CharField('Meal chosen by Person',
                                       max_length=3,
                                       null=True,
                                       choices=MEAL_CHOICES,
                                       default=MEAL_CHOICES[0][0])
    music_preference = models.CharField('Music chosen by person',
                                        null=True,
                                        max_length=500)
