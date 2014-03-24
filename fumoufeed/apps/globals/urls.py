#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2014 george 
#
# Distributed under terms of the MIT license.

from django.conf.urls import patterns
from views import IndexView

urlpatterns = patterns('',
    (r'^$', IndexView.as_view()),
)

