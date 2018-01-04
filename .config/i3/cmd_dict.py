chromium = (
    'chromium --new-window --load-extension=/home/cheese/.cache/wal/wal_chrome'
)

cmd_dict = {
    1: chromium,
    2: 'subl',
    3: 'urxvt',
    10: chromium + ' --incognito https://www.reddit.com/',
}
