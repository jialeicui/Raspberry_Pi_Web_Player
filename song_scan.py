import os

def get(base_dir, opt_dir = ''):
    ret = []
    final_dir = os.path.join(base_dir, opt_dir)
    if os.path.isfile(final_dir):
        return  play(final_dir)
    for dirs in os.listdir(final_dir):
        if not dirs.startswith('.'):
            if os.path.isdir(os.path.join(final_dir, dirs)):
                ret.append({'name':dirs, 'href':'/ls/' + os.path.join(opt_dir, dirs), 'playable':False})
            elif _is_audio_file(dirs):
                ret.append({'name':dirs, 'href':'/play/' + os.path.join(opt_dir, dirs), 'playable':True})
    return ret
    pass

def play(f):
    return []
    pass

def _is_audio_file(name):
    valid_ext = ['mp3', 'm4a', 'ape', 'wma']
    n, ext = os.path.splitext(name)
    if valid_ext.count(ext[1:].lower()) != 0:
        return True
    return False
    pass