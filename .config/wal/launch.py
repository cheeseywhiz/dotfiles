#!/usr/bin/env python3
"""Centralized and standardized wal launch process"""
import argparse
import os
import pathlib
import subprocess
import sys

WAL_CACHE = pathlib.Path.home() / '.cache/wal'


def path_type(path):
    return os.path.abspath(os.path.expanduser(path))


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


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    arg = argparse.ArgumentParser(description=__doc__)

    arg.add_argument(
        'path', type=path_type,
        help='Path given directly to wal -i.')

    args = arg.parse_args(argv)
    wal(args.path)


if __name__ == '__main__':
    main()
