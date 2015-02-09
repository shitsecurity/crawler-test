#!/usr/bin/env python

from bottle import route, view
from bottle import static_file as file

@route('/sitemap.xml', name='sitemap')
def sitemap():
	return file('sitemap.xml','public')

@route('/sitemap/file')
@route('/sitemap/folder/')
@view('templates/sitemap/index.tpl')
def sitemap_files(): return {}
