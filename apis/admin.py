# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from apis.models import Gateway

class GatewayAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'endpoint',)

admin.site.register(Gateway, GatewayAdmin)
