from django.db import models

from base.models import BaseModel



class Group(BaseModel):
    name = models.CharField(max_length=255)


class User(BaseModel):
    name = models.CharField(max_length=255)
    groups = models.ManyToManyField(Group, blank=True)


    def __str__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }
