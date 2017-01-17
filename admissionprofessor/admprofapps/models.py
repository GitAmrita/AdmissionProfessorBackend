from __future__ import unicode_literals

from django.db import models


class Member(models.Model):
    email = models.CharField(max_length=100)
    screen_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    create_date = models.DateTimeField('member since')

    def __str__(self):
        return self.screen_name + ': ' + self.email
