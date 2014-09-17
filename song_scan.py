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
            else:
                ret.append({'name':dirs, 'href':'/play/' + os.path.join(opt_dir, dirs), 'playable':True})
    return ret
    pass

def play(f):
    return []
    pass
