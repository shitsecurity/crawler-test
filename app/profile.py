#!/usr/bin/env python

from bottle import route, view

from auth import acl, Roles

@route('/profile', method=['GET'], name='profile')
@view('templates/profile/index.tpl')
@acl( Roles.USER )
def profile_index(): return {}

@route('/profile/settings', method=['GET'], name='settings')
@view('templates/profile/index.tpl')
@acl( Roles.USER )
def profile_settings(): return {}

@route('/profile/history', method=['GET'], name='history')
@view('templates/profile/index.tpl')
@acl( Roles.USER )
def profile_history(): return {}

@route('/profile/subscriptions', method=['GET'], name='subscriptions')
@view('templates/profile/index.tpl')
@acl( Roles.USER )
def profile_subscriptions(): return {}

@route('/profile/billing', method=['GET'], name='billing')
@view('templates/profile/index.tpl')
@acl( Roles.USER )
def profile_billing(): return {}

@route('/profile/transactions', method=['GET'], name='transactions')
@view('templates/profile/index.tpl')
@acl( Roles.USER )
def profile_transactions(): return {}

@route('/profile/messages', method=['GET'], name='messages')
@view('templates/profile/index.tpl')
@acl( Roles.USER )
def profile_messages(): return {}

@route('/profile/photos', method=['GET'], name='photos')
@view('templates/profile/index.tpl')
@acl( Roles.USER )
def profile_photos(): return {}

@route('/profile/files', method=['GET'], name='files')
@view('templates/profile/index.tpl')
@acl( Roles.USER )
def profile_files(): return {}

@route('/profile/memos', method=['GET'], name='memos')
@view('templates/profile/index.tpl')
@acl( Roles.USER )
def profile_memos(): return {}

@route('/profile/tags', method=['GET'], name='tags')
@view('templates/profile/index.tpl')
@acl( Roles.USER )
def profile_tags(): return {}

@route('/profile/posts', method=['GET'], name='posts')
@view('templates/profile/index.tpl')
@acl( Roles.USER )
def profile_posts(): return {}
