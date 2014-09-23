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

header = {'Host':'music.163.com', 
          'Referer':'http://music.163.com/'}

def post(url, data):
    request = urllib2.Request(url)
    for k,v in header.items():
        request.add_header(k, v)

    f = urllib2.urlopen(
        request,
        data = urllib.urlencode(data))

    return f.read()
    pass

def get(url):
    request = urllib2.Request(url)
    for k,v in header.items():
        request.add_header(k, v)

    f = urllib2.urlopen(request)

    return f.read()
    pass

class index:
    def GET(self, opt_dir = ''):
        return render.index([])

class search:
    def POST(self):
        keyword = web.input()['keyword'].encode('utf-8')
        songs = []
        try:
            res = self.search(keyword)
            for r in res:
                show_title = '%s - %s' % (r['name'], r['artists'][0]['name'])
                songs.append({'href':'/player/play', 'addhref':'/player/add', 'file_path':self._get_song_url(r['id']), 'name':show_title})
                pass
        except:
            pass
        return render.index(songs)
        pass
    def _get_results(self, context):
        p = json.loads(context)['result']
        return p['songs']
        pass

    def search(self, name):
        url  = 'http://music.163.com/api/search/suggest/web?csrf_token='
        data = {'s': name,
                'limit':8}

        return self._get_results(post(url, data))
        pass
    def _get_song_url(self, id):
        url = 'http://music.163.com/api/song/detail?ids=[%d]' % id
        context = get(url)
        p = json.loads(context)['songs'][0]['mp3Url']
        return p[len('http://'):]
        pass

app_netease = web.application(urls, locals())
