#!/usr/bin/env python

from bottle import route, view

from utils import get_url

import string
import random

@route('/depth', name='depth')
@route('/depth/<path:path>')
@view('templates/depth/index.tpl')
def depth( path='' ):
	filename = lambda: ''.join([random.choice(string.letters)
								for _ in xrange(random.randrange(6,13))])
	links = [ '/'.join( filter( lambda p: p!='',
								[ get_url('depth'), path, filename() ]))
			for _ in xrange(random.randrange(4,9)) ]
	return dict(links=links)
