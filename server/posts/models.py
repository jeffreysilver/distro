from django.db import models

from base.models import BaseModel
from users.models import User, Group


class Post(BaseModel):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name="posts", on_delete=models.CASCADE)
    link = models.URLField()

