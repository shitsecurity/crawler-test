#!/usr/bin/env python

from bottle import error, view

@error(404)
@view('templates/error/404.tpl')
def error404( error ):
	return dict(error=error)

@error(403)
@view('templates/error/403.tpl')
def error403( error ):
	return dict(error=error)
