# -*- coding:utf8 -*-

import web
import song_scan
import netease
import douban_fm
import player

# web.config.debug = False 
render = web.template.render('templates/')
base_dir = '/Users/jialeicui/Music'
mplayer_sub = None

urls = (
    '/', 'index',
    '/ls/(.*)', 'index',
    '/player', player.app_player,
    '/net', netease.app_netease,
    '/douban', douban_fm.app_douban,
)

class index:
    def GET(self, opt_dir = ''):
        ll = song_scan.get(base_dir, opt_dir)
        return render.index(ll)


if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()
