from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="sheqmnis tarigi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="ganaxlebis tarigi")

    class Meta:
        abstract = True