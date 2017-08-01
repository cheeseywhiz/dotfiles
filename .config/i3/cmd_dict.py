cmd_dict = {
    None: {
        'cmd': ['bash', '-c', 'exec'],
        'msg': {
            'long': None,
            'short': None,
            'color': None,
            't': None,
        },
    },
    1: {
        'cmd': ['chromium', 'https://www.reddit.com/'],
        'msg': {
            'long': 'Opening Firefox',
            'short': 'Firefox',
            'color': None,
            't': 3,
        },
    },
    2: {
        'cmd': ['subl3'],
        'msg': {
            'long': 'Opening Sublime',
            'short': 'Sublime',
            'color': None,
            't': 3,
        },
    },
    3: {
        'cmd': ['urxvt'],
        'msg': {
            'long': 'Opening URxvt',
            'short': 'URxvt',
            'color': None,
            't': 3,
        },
    },
    4: {
        'cmd': ['gitkraken'],
        'msg': {
            'long': 'Opening GitKraken',
            'short': 'GitKraken',
            'color': None,
            't': 3,
        },
    },
    10: {
        'cmd': ['chromium', '--incognito', 'https://www.reddit.com/'],
        'msg': {
            'long': 'Opening private Firefox window',
            'short': 'Firefox private',
            'color': None,
            't': 3,
        },
    },
}
