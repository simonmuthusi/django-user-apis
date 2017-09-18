# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Gateway(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    endpoint = models.CharField(max_length=255)
