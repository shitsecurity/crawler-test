#!/usr/bin/env python

from bottle import route, view

@route('/submit', method=['GET'], name='submit_form')
@view('templates/submit/form.tpl')
def submit_form(): return {}

@route('/submit', method=['POST'], name='submit')
@view('templates/submit/index.tpl')
def submit(): return {}
