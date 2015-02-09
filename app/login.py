#!/usr/bin/env python

from bottle import route, view
from bottle import response, request
from bottle import default_app as app
from bottle import abort

get_url = app().get_url

from auth import secret, Roles, create_token

@route('/login', method=['GET'], name='login_form')
@view('templates/login/form.tpl')
def login_form():
    return dict()

@route('/login', method=['POST'], name='login')
@view('templates/login/index.tpl')
def login():
	response.set_cookie('auth',True,secret)
	response.set_cookie('role',Roles.USER,secret)
	response.status = 303
	response.set_header('Location',get_url('profile'))
	return dict()

@route('/logout', method=['GET'], name='logout')
@view('templates/login/logout.tpl')
def logout():
	response.delete_cookie('auth')
	response.delete_cookie('role')
	response.status = 303
	response.set_header('Location',get_url('index'))
	return dict()

@route('/login_csrf', method=['GET'], name='login_form_csrf')
@view('templates/login/form_csrf.tpl')
def login():
	token = create_token()
	response.set_cookie('token',token,secret)
	return dict(token=token)

@route('/login_csrf', method=['POST'], name='login_csrf')
@view('templates/login/index.tpl')
def login():
	response.set_cookie('auth',True,secret)
	response.set_cookie('role',Roles.USER,secret)
	token = request.get_cookie('token',secret=secret)
	token = request.forms.get('token')
	if token!=token:
		abort(403,'Invalid Token: {}'.format(token))
	response.delete_cookie('token')
	response.status = 303
	response.set_header('Location',get_url('profile'))
	return dict()
