#!/usr/bin/env python

from bottle import route, view
from bottle import request

@route('/get', method=['GET'], name='get')
@view('templates/get/index.tpl')
def get_param():
	return dict(p1=request.query.get('p1',''),
				p2=request.query.get('p2',''))
