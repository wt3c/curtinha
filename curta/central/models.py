from django.db import models
from django.contrib.auth.models import User


class Curtinha(models.Model):
    owner = models.ForeignKey(User, blank=True, null=True)
    url_original = models.URLField()
    url_curta = models.URLField(max_length=50)

    def __str__(self):
        return self.url_curta
