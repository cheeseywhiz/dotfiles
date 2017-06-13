from csv import writer
from time import time

PIPE = '/home/cheese/.i3blocks/sys-msg/pipe'


def write(long: str, short: str, color: str=None, t: int=None) -> None:
    """
    Write a message to the status bar for a given amount of time.
    """
    with open(PIPE, 'w') as csvfile:
        file = writer(csvfile)
        file.writerow(['time', 't-limit', 'long', 'short', 'color'])
        file.writerow([time(), t, long, short, color])


def clear():
    """
    Clear the status bar at any given time.
    """
    with open(PIPE, 'w') as csvfile:
        file = writer(csvfile)
        file.writerow(['time', 't-limit', 'long', 'short', 'color'])
        file.writerow([time(), *[None] * 4])
