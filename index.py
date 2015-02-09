#!/usr/bin/env python

from bottle import route, run
from bottle import error, abort
from bottle import template, view
from bottle import request, response
from bottle import get, post

import app.index
import app.assets
import app.help
import app.login
import app.profile
import app.depth
import app.robots
import app.sitemap
import app.error
import app.mixed
import app.cycle
import app.secret
import app.submit
import app.get

run(host='localhost', port=8080, debug=True, reloader=True)
