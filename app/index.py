#!/usr/bin/env python

from bottle import route, view

@route('/', method=['GET'], name='index')
@view('templates/index/index.tpl')
def index(): return {}
