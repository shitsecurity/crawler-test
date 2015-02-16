#!/usr/bin/env python

from bottle import error, view, route

@error(404)
@view('templates/error/404.tpl')
def error404( error ):
	return dict(error=error)

@error(403)
@view('templates/error/403.tpl')
def error403( error ):
	return dict(error=error)

@route('/<route:path>')
@view('templates/error/404.tpl')
def error404_200(route):
	return {}
