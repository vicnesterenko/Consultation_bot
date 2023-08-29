from django.db import models

# from django.urls import reverse


class MyTable(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_id = models.IntegerField()
    text = models.CharField(max_length=100)
    # …

    # # Methods
    # def get_absolute_url(self):
    #     """Returns the URL to access a particular instance of MyModelName."""
    #     return reverse('model-detail-view', args=[str(self.id)])

    # def __str__(self):
    #     """String for representing the MyModelName object (in Admin site etc.)."""
    #     return self.name


class Question(models.Model):
    # Fields
    q_id = models.CharField(max_length=100)
    q = models.TextField()
    img = models.TextField(blank=True)

    # def __str__(self):
    #     return self.name


class Option(models.Model):
    # Fields
    label = models.CharField(max_length=100)
    next_id = models.CharField(max_length=100)
    order = models.IntegerField()

    # def __str__(self):
    #     return self.name


class Link(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    url = models.TextField()

    # def __str__(self):
    #     return self.__class__.name
