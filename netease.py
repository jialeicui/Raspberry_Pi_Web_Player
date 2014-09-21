# -*- coding:utf8 -*-

import urllib2
import urllib
import json
import web

urls = (
    '', 'index',
    '/search', 'search',
)

render = web.template.render('templates/netease')

class index:
    def GET(self, opt_dir = ''):
        return render.index([])

class search:
    def POST(self):
        res = self.search(web.input()['keyword'])
        songs = []
        for r in res:
            songs.append({'href':'/playurl/'+self._get_song_url(r['id']), 'name':r['name']})
            pass
        return render.index(songs)
        pass
    def _get_results(self, context):
        p = json.loads(context)['result']
        return p['songs']
        pass

    def search(self, name):
        url  = 'http://music.163.com/api/search/suggest/web?csrf_token='
        request = urllib2.Request(url)
        request.add_header('Host', 'music.163.com')
        request.add_header('Referer', 'http://music.163.com/')

        data = {'s': name,
                'limit':8}
        f = urllib2.urlopen(
            request,
            data = urllib.urlencode(data))

        return self._get_results(f.read())
        pass
    def _get_song_url(self, id):
        url = 'http://music.163.com/api/song/detail?ids=[65053]'
        request = urllib2.Request(url)
        request.add_header('Host', 'music.163.com')
        request.add_header('Referer', 'http://music.163.com/')
        f = urllib2.urlopen(request).read()
        p = json.loads(f)['songs'][0]['mp3Url']
        return p[len('http://'):]
        pass


app_netease = web.application(urls, locals())