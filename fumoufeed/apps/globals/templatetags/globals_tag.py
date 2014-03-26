#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2014 george 
#
# Distributed under terms of the MIT license.
import dot
import codecs
import os
from django import template

import pdb;pdb.set_trace()
register = template.Library()

app_path = os.path.join(os.path.dirname(__file__), '../') 
template_path = os.path.join(app_path, 'templates/globals/dot')


@register.filter
def js_template(js_file):
    js_file = os.path.join(template_path, js_file)
    return dot.template(codecs.open(js_file,'r','utf8').read())

