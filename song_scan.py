import os

def get(base_dir, opt_dir = ''):
    folders = []
    songs = []

    final_dir = os.path.join(base_dir, opt_dir)

    for dirs in os.listdir(final_dir):
        if not dirs.startswith('.'):
            if os.path.isdir(os.path.join(final_dir, dirs)):
                folders.append({'name':dirs, 'href':'/ls/' + os.path.join(opt_dir, dirs),'playable':False})
            elif _is_audio_file(dirs):
                songs.append({'name':dirs, 'file_path':os.path.join(opt_dir, dirs), 'href':'/player/play', 'addhref':'/player/add','playable':True})

    folders.sort()
    songs.sort()

    return folders + songs
    pass


def _is_audio_file(name):
    valid_ext = ['mp3', 'm4a', 'ape', 'wma', 'flac']
    n, ext = os.path.splitext(name)
    if valid_ext.count(ext[1:].lower()) != 0:
        return True
    return False
    pass