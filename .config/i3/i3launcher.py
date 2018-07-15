#!/usr/bin/env python3
import json
import os
import pathlib
import shlex
import subprocess

ws_cmd = subprocess.Popen(
    ['i3-msg', '-t', 'get_workspaces'],
    stdout=subprocess.PIPE)
ws_data = ws_cmd.communicate()[0].decode()
ws_dict = json.loads(ws_data)

current_ws = next(i['num'] for i in ws_dict if i['visible'])
launch_cmd = os.getenv('WS' + str(current_ws))

if launch_cmd is not None:
    subprocess.Popen(shlex.split(launch_cmd))
    print(f'{pathlib.Path(__file__).name}: ran {launch_cmd}')
