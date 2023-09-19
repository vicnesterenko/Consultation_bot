import uuid
from django.db import models

# from django.urls import reverse


# class MyTable(models.Model):
#    """A typical class defining a model, derived from the Model class."""

# Fields
#    my_id = models.IntegerField()
#    text = models.CharField(max_length=100)
# …

# # Methods
# def get_absolute_url(self):
#     """Returns the URL to access a particular instance of MyModelName."""
#     return reverse('model-detail-view', args=[str(self.id)])

# def __str__(self):
#     """String for representing the MyModelName object (in Admin site etc.)."""
#     return self.name


class Questions(models.Model):
    # Fields
    q_id = models.CharField(max_length=100)
    text = models.TextField()
    img_id = models.TextField(blank=True)
    created_at = models.DateTimeField()

    # def __str__(self):
    #     return self.name


class Images(models.Model):
    img_id = models.CharField(max_length=100)
    img_path = models.CharField(max_length=100)
    created_at = models.DateTimeField()


class Option(models.Model):
    # Fields
    label = models.CharField(max_length=100)
    next_id = models.CharField(max_length=100)
    order = models.IntegerField()

    # def __str__(self):
    #     return self.name


class Links(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    url = models.TextField()

    # def __str__(self):
    #     return self.__class__.name
