#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2014 george 
#
# Distributed under terms of the MIT license.

from django.conf.urls import patterns
from apps.fumoufeed.views import PeopleApi, PostApi

urlpatterns = patterns('',
    (r'^people/(\w+)', PeopleApi.as_view()),
    (r'^people/', PeopleApi.as_view()),
    (r'^post/list', PostApi.list),
    (r'^post/(\w+)', PostApi.as_view()),
    (r'^post', PostApi.as_view()),
)

