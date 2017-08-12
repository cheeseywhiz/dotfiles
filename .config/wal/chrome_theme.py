#!/usr/bin/env python3
# TODO: generate images by tinting a grayscale theme according to wal palatte
import json
import os
from pywal.settings import CACHE_DIR


def fix_hex_str(hex_str):
    if hex_str[0] == '#':
        yield from hex_str
    else:
        yield '#'
        yield from hex_str


def hex_rgb(hex_str):
    return eval('(0x{1}{2}, 0x{3}{4}, 0x{5}{6})'.format(*fix_hex_str(hex_str)))


def wal_palatte():
    colors_path = os.path.join(CACHE_DIR, 'colors.json')
    with open(colors_path) as file:
        wal_palatte = json.loads(file.read())['colors']

    return {name: hex_rgb(color)
            for name, color in wal_palatte.items()}


def manifest_json(palatte):
    return json.dumps({
        'manifest_version': 2,
        'name': 'wal_chrome',
        'version': '1.0',
        'theme': {
            'colors': {
                'frame': palatte['color1'],
                'toolbar': palatte['color0'],
                'tab_text': palatte['color7'],
                'tab_background_text': palatte['color8'],
                'bookmark_text': palatte['color7'],
                'ntp_background': palatte['color0'],
                'ntp_text': palatte['color7'],
            }, }, })


def main():
    palatte = wal_palatte()
    json_path = os.path.join(CACHE_DIR, 'wal_chrome', 'manifest.json')
    with open(json_path, 'w') as file:
        file.write(manifest_json(palatte))


if __name__ == '__main__':
    main()
