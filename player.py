# -*- coding:utf8 -*-

import os
import web
import player_core

web.config.debug = False 
player_core = player_core.player()
render = web.template.render('templates/playlist')

urls = (
    '/play', 'play',
    '/add', 'modify',
    '/remove', 'modify',
    '/control', 'control',
    '/show', 'show'
)

base_dir = '/Users/jialeicui/Music'

class play:
    def POST(self):
        post = web.input()
        if post['position'] == 'local':
            player_core.play(os.path.join(base_dir, post['path']))
        elif post['position'] == 'remote':
            player_core.play('http://' + post['path'])
        return ''

class modify:
    def POST(self):
        post = web.input()
        action = post['action']
        if action == 'add':
            source = ''
            if post['position'] == 'local':
                source = os.path.join(base_dir, post['path'])
            elif post['position'] == 'remote':
                source = 'http://' + post['path']

            player_core.add(source, post['title'])
        elif action == 'remove':
            return player_core.remove(int(post['id']))
        return ''

class control:
    def POST(self):
        post = web.input()
        if post['action'] == 'next':
            player_core.next()
            pass
        return ''

class show:
    def GET(self):
        plist = player_core.get_list()
        for x in xrange(0, len(plist)):
            plist[x]['id'] = x
            pass
        return render.index(plist)

app_player = web.application(urls, locals())
