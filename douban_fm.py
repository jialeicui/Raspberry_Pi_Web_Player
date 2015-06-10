# -*- coding:utf8 -*-

import http_method
import json
import web

urls = (
    '', 'index',
)

channel_url = 'http://www.douban.com/j/app/radio/people?app_name=radio_desktop_win&version=100&channel=%d&type=n'
render = web.template.render('templates/douban')


class index:
    def GET(self, opt_dir = ''):
        songs = self._get_playlist(1)
        # return songs
        return render.index(songs)

    def _get_playlist(self, channel):
        content = http_method.get(channel_url % channel)
        ret = json.loads(content)
        if ret['r'] != 0:
            return []
        return ret['song']


app_douban = web.application(urls, locals())
