#!/usr/bin/env python

from bottle import default_app, BaseTemplate

get_url = default_app().get_url

BaseTemplate.defaults['get_url'] = get_url
