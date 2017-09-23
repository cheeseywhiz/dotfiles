#!/usr/bin/env python3
# TODO: generate images by tinting a grayscale theme according to wal palatte
import json
import os
import subprocess
import sys
from pywal.settings import CACHE_DIR


def call(*args, **Popen_kwargs):
    proc = subprocess.Popen([*args], **Popen_kwargs)
    ret_code = proc.wait()

    if ret_code:
        sys.exit(ret_code)
    else:
        return proc


def ntp_background():
    with open(os.path.join(CACHE_DIR, 'wal')) as file:
        wal_img = file.read()

    call('convert', wal_img, '-scale', '1366x768^', '-blur', '0x10',
         os.path.join(CACHE_DIR, 'wal_chrome/img/theme_ntp_background.jpg'))


def wal_palatte():
    with open(os.path.join(CACHE_DIR, 'colors.json')) as file:
        palatte = json.load(file)['colors']

    return {name: eval('(0x{1}{2}, 0x{3}{4}, 0x{5}{6})'.format(*color))
            for name, color in palatte.items()}


def manifest(palatte):
    return {
        'manifest_version': 2,
        'name': 'wal_chrome',
        'version': '1.0',
        'theme': {
            'images': {
                'theme_ntp_background': 'img/theme_ntp_background.jpg'
            },
            'colors': {
                'frame': palatte['color1'],
                'toolbar': palatte['color0'],
                'tab_text': palatte['color7'],
                'tab_background_text': palatte['color8'],
                'bookmark_text': palatte['color7'],
                'ntp_background': palatte['color0'],
                'ntp_text': palatte['color7'],
            },
            'properties': {
                'ntp_background_repeat': 'no-repeat',
                'ntp_background_alignment': 'middle middle',
                'ntp_logo_alternate': 0,
            }, }, }


def main():
    ntp_background()
    json_path = os.path.join(CACHE_DIR, 'wal_chrome/manifest.json')

    with open(json_path, 'w') as file:
        json.dump(manifest(wal_palatte()), file)


if __name__ == '__main__':
    main()
