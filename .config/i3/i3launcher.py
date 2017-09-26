#!/usr/bin/env python3
import json
import pathlib
import shlex
import subprocess
from cmd_dict import cmd_dict

ws_cmd = subprocess.Popen(
    ['i3-msg', '-t', 'get_workspaces'],
    stdout=subprocess.PIPE)
ws_data = ws_cmd.communicate()[0].decode()
ws_dict = json.loads(ws_data)

current_ws = next(i['num'] for i in ws_dict if i['visible'])
launch_cmd = cmd_dict.get(current_ws, NotImplemented)

if launch_cmd is not NotImplemented:
    subprocess.Popen(shlex.split(launch_cmd))
    print(f'{pathlib.Path(__file__).name}: ran {launch_cmd}')
