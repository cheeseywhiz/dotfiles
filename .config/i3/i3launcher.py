#!/usr/bin/env python3
import json
import pathlib
import subprocess
from cmd_dict import cmd_dict

unspecified = object()

ws_cmd = subprocess.Popen(
    ['i3-msg', '-t', 'get_workspaces'],
    stdout=subprocess.PIPE)
ws_data = ws_cmd.communicate()[0].decode()
ws_dict = json.loads(ws_data)

current_ws = next(i['num'] for i in ws_dict if i['visible'])
launch_cmd = cmd_dict.get(current_ws, unspecified)

if launch_cmd is not unspecified:
    subprocess.Popen([*launch_cmd])
    print(f"{pathlib.Path(__file__).name}: ran {' '.join(launch_cmd)}")
