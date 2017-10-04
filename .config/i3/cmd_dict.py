chromium = (
    'chromium --new-window --load-extension=/home/cheese/.cache/wal/wal_chrome'
)

cmd_dict = {
    1: chromium,
    2: 'bash -c "subl |& sudo tee /var/subllog > /dev/null"',
    3: 'urxvt',
    4: 'gitkraken',
    10: chromium + ' --incognito https://www.reddit.com/',
}
