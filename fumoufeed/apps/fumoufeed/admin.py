#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2014 george 
#
# Distributed under terms of the MIT license.


from django.contrib import admin
from apps.fumoufeed.models import People, Post

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('fuid', 'title')

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'fpid', 'priority', 'live', 'create_time')

admin.site.register(People, PeopleAdmin)
admin.site.register(Post, PostAdmin)

