from django.db import models


class Link(models.Model):
    short_link = models.CharField(max_length=8, primary_key=True)
    httpurl = models.URLField(max_length=264, verbose_name="Full URL", unique=True)

    def __str__(self):
        return self.httpurl

