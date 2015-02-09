#!/usr/bin/env python

from bottle import route, static_file as file

@route('/assets/<path:path>', name='assets')
def static( path ):
	return file(path,root='public')
