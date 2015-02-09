#!/usr/bin/env python

from bottle import route, view
from bottle import static_file as file

@route('/robots.txt', name='robots')
def robots():
	return file('robots.txt','public')

@route('/allow/file')
@route('/allow/folder/')
@route('/disallow/file')
@route('/disallow/folder/')
@view('templates/robots/index.tpl')
def robot_files(): return {}
