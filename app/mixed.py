#!/usr/bin/env python

from bottle import route, view, abort

from auth import authed, Roles
from utils import get_url

@route('/mixed', name='mixed')
@view('templates/mixed/index.tpl')
def mixed():
	if not authed(Roles.USER):
		abort(404,'Not Found')
	return {}
