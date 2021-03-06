#!/usr/bin/env sh

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -x polybar >& /dev/null; do
    sleep 0.1
done

# Launch top bar
polybar -r top &
