#!/usr/bin/env python3
import pathlib
import subprocess
import sys

WAL_CACHE = pathlib.Path.home() / '.cache/wal'


def call(*args, **Popen_kwargs):
    proc = subprocess.Popen([*args], **Popen_kwargs)
    ret_code = proc.wait()

    if ret_code:
        sys.exit(ret_code)
    else:
        return proc


def wal(path):
    call('wal', '-i', path, '-a', '93')

    with open(WAL_CACHE / 'wal') as file:
        wal_img = file.read()

    call('convert', wal_img, '-scale', '1366x768^', '-blur', '0x10',
         WAL_CACHE / 'wal_chrome/img/theme_ntp_background.jpg')
    call(pathlib.Path.home() / '.config/wal/chrome_theme.py')


def main(_, path):
    wal(path)


if __name__ == '__main__':
    main(*sys.argv)
