# -*- coding:utf8 -*-

import web
import song_scan
import os
import subprocess
import netease

render = web.template.render('templates/')
base_dir = '/Users/jialeicui/Music'
mplayer_sub = None

urls = (
    '/', 'index',
    '/ls/(.*)', 'index',
    '/play/(.*)', 'play',
    '/playurl/(.*)', 'playurl',
    '/net', netease.app_netease,
)

class index:
    def GET(self, opt_dir = ''):
        ll = song_scan.get(base_dir, opt_dir)
        return render.index(ll)

class play:
    def GET(self, opt_dir = ''):
        os.system('killall mplayer')
        subprocess.Popen('mplayer "' + os.path.join(base_dir, opt_dir) + '"', shell=True)
        return ''

class playurl:
    def GET(self, url = ''):
        url = 'http://' + url
        mp = globals()['mplayer_sub']
        # return os.path.join(base_dir, opt_dir)
        if mp:
            mp.terminate()
            os.system('killall mplayer')
        globals()['mplayer_sub'] = subprocess.Popen('mplayer ' + url, shell=True)
        return ''

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()
