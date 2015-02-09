#!/usr/bin/env python

from bottle import route, view

from utils import get_url

@route('/cycle', name='cycle')
@route('/cycle/')
@route('/cycle/<link>')
@view('templates/cycle/index.tpl')
def cycle( link='' ):
	links = {
            '':    '123',
            '123': 'abc',
            'abc': '000',
            '000': '123'
	}
	return dict(next='{}/{}'.format( get_url('cycle'), links[link] ))
