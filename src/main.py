#!/usr/bin/env python3

import os
import sys
import yaml


def config():
  with open('cmd.yml') as file:
    return yaml.full_load(file)

def run():
  cmds = config()
  args = sys.argv[1:]
  cmd = args.pop(0) if len(args) else ''
  command = args.pop(0) if len(args) else ''

  os.system("uptime")
  print(cmd, command, args)

  if command.startswith('-', 0, 1):
    args.insert(0, command)
    command = ''

  if cmd in cmds.keys():
    commands = cmds[cmd]['commands'] if 'commands' in cmds[cmd].keys() else cmds[cmd]

    if command in commands.keys():
      actions = commands[command] if type(commands[command]) is list else [commands[command]]

      for action in actions:
        print(action)
        os.system(action)

    else:
      print("action not found")

  else:
    print("command not found.")
