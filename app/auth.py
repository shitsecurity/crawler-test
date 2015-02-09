#!/usr/bin/env python

from bottle import request, abort

import os

secret=os.urandom(64)

class Roles( object ):
    NOBODY = 0
    USER   = 1
    ADMIN  = 2

from functools import wraps

def authed( *roles ):
	auth = request.get_cookie('auth',secret=secret)
	role = request.get_cookie('role',secret=secret)
	if auth==True and role in roles:
		return True
	else:
		return False

def acl( *roles ):
	def decorator( f ):
		@wraps( f )
		def wrapper( *args, **kwargs ):
			if authed( *roles ):
				return f( *args, **kwargs )
			else:
				abort(code=403,text='Access Denied')
		return wrapper
	return decorator

def create_token(): return os.urandom(32).encode('base64')
