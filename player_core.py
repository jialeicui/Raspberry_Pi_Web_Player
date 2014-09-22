import time
import threading
import subprocess

class player(object):
    def __init__(self):
        print 'init'
        self.playlist = []
        self.handle = None
        self._start()
        pass

    def __del__(self):
        del self.t
        pass

    def _player_thread(self):
        while True:
            if self.playlist:
                self._play(self.playlist.pop(0))
        pass

    def _start(self):
        self.t = threading.Thread(target=self._player_thread, args=())
        self.t.start()
        pass

    def _play(self, source):
        self.handle = subprocess.Popen(['mplayer',source], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        while True:
            time.sleep(1)
            for l in self.handle.stdout:
                if l.startswith('Exit'):
                    return
                    break
                pass
            pass
        pass

    def play(self, source):
        self.playlist.insert(0, source)
        self.next()
        pass

    def add(self, source):
        self.playlist.append(source)
        pass

    def next(self):
        self.handle.stdin.write('q')

    def remove(self, id):
        if id < len(self.playlist):
            self.playlist.pop(id)
            pass
        pass

    def get_list(self):
        return self.playlist
        pass

if __name__ == '__main__':
    p = player()
    time.sleep(5)
    p.add('http://m1.music.126.net/76Tcz9oo83Diol_rTKPJ8g==/1187472558006034.mp3')
    p.add('/Users/jialeicui/Music/Drive By.mp3')
    time.sleep(5)
    p.next()
    time.sleep(5)


