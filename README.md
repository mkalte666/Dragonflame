# Dragonflame
An IRCBot written in Python

## What is this?
I always wonderd why people use irssi and perl to build IRC Bots. 
Today I was bored so I created Dragonflame: An IRCBot that only uses the standard library of Python!

## How to Use?
In the Dragonflame.py change the server settings, nickname, channelname, ... to things you need/want and run it!
You can either edit Dragonflame.py to add (LoadModule(name)) modules or you can do it at runtime via the "load <name>" command.
Stopping the bot can be done by entering CTRL-C

Some foo i wrote for a friend on IRC:

### Base Stuff
So Dragonflame normally loads modules and adds the HandlerFunc of that module to the IrcClient via RegisterEventHandler.
An example file would be
     
    # coding=utf-8
    import random
    import re
    import IrcClient
    import worddb
    import imp
    import sys
 
    def HandlerFunc(client, event, prefix, command, params, trailing):
        if params != client.nick:
                if command == "PRIVMSG":
                        client.SendMessage(params, trailing)
 
THIS HANDLER echos everything - a bit annoying but a good example. PRIVMSG is the command - params for that command is the sender - a channel or a user. trailing is the message.
now you could parse trailing for things, as i do in the many handers.
 
the handler func itself can be added without the module stuff - you could put it in dragonflame.py and just call client.RegisterEventHandler(funcname).
Woop woop.
The rest is up to you :D

### Copying
See LICENSE
