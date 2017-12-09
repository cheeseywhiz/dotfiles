#!/usr/bin/env sh

# Terminate already running bar instances
killall -q devilspie2

# Wait until the processes have been shut down
while pgrep -x devilspie >& /dev/null; do
    sleep 0.1
done

# Launch top bar
devilspie2 &
