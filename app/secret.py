#!/usr/bin/env python

from bottle import route, view

@route('/secret', name='secret')
@route('/secret/')
@route('/secret/secret')
@view('templates/secret/index.tpl')
def secret(): return {}
