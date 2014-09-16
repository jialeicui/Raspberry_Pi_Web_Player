import web
import song_scan
import os

render = web.template.render('templates/')
base_dir = '/Users/jialeicui/Music'

urls = (
    '/', 'index',
    '/ls/(.*)', 'index',
    '/play/(.*)', 'play',
)

class index:
    def GET(self, opt_dir = ''):
        ll = song_scan.get(base_dir, opt_dir)
        return render.index(ll)

class play:
    def GET(self, opt_dir = ''):
        # return os.path.join(base_dir, opt_dir)
        return os.system('open "' + os.path.join(base_dir, opt_dir) + '"')

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()
