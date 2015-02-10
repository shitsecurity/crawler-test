#!/usr/bin/env python

from bottle import route, view

@route('/width', method=['GET'], name='width')
@view('templates/width/index.tpl')
def width(): return dict(amount=256)

@route('/width<link>', method=['GET'])
@view('templates/width/index.tpl')
def width(link): return dict()
