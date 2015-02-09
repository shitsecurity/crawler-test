#!/usr/bin/env python

from bottle import route, view

@route('/help', method=['GET'], name='help')
@view('templates/help/index.tpl')
def help(): return {}
