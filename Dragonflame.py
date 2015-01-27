#!/usr/bin/python3
# coding=utf-8
import random
import re
import IrcClient
import worddb
import imp
import sys
	
client = IrcClient.IrcClient("irc.mibbit.net", 6667, "Dragonflame", "DragonBot@invalid", False, True)

client.AddIgnore("Moberry")
client.AddIgnore("Droplet")
client.AddIgnore("Mesril")

def ReloadModule(name):
	try:
		moduleToReload = sys.modules[name]
		if(name!="worddb"):
			client.RemoveEventHandler(moduleToReload.HandlerFunc)
		imp.reload(moduleToReload)
		if(name!="worddb"):
			client.RegisterEventHandler(moduleToReload.HandlerFunc)
	except:
		print("Could Reload "+name+"! Is there a HandlerFunc? Did you even load the module?")
		pass

def LoadModule(name):
	try:
		moduleToLoad = sys.modules[name]
		client.RemoveEventHandler(moduleToLoad.HandlerFunc)
		imp.reload(moduleToLoad)
		client.RegisterEventHandler(moduleToLoad.HandlerFunc)
	except:
		pass
		
	fp, pathname, description = imp.find_module(name)
	
	try:
		moduleToLoad = imp.load_module(name, fp, pathname, description)
		client.RegisterEventHandler(moduleToLoad.HandlerFunc)
	except: 
		print ("Could not load "+name+"! Is there a HandlerFunc? Does it even exist?!?")
		pass
	finally:
		if fp:
			fp.close()

LoadModule("HelloHandler")
LoadModule("PokeHandler")
LoadModule("TalkAboutYourselfHandler")

client.JoinChannel("#exploders")
client.SendMessage("#exploders", "*yawns* hello people")

e = re.compile(ur'(\w*)\s*([\w@.#,:()"\'$%&\/\[\] -]*)')

while True:
	cmd = ""
	arg = ""
	inCmd = raw_input("CMD?: ")
	match = e.search(inCmd)
	cmd=match.group(1)
	arg = match.group(2)
	
	if cmd=="reload":
		ReloadModule(arg)
	elif cmd=="load":
		LoadModule(arg)
	elif cmd=="nick":
		client.SetNick(arg)
	elif cmd=="identify":
		client.Identify(arg)
	elif cmd=="exit" or cmd=="kill" or cmd=="quit":
		exit()
	elif cmd=="say":
		try:
			channel, sendArg = arg.split(' ', 1)
			client.SendMessage(channel, sendArg)
		except:
			print("WARNING: invalid syntax for say! say <channel> <message>")
			pass
	elif cmd=="broadcast":
		client.BroadcastMessage(arg)
	elif cmd=="join":
		client.JoinChannel(arg)
	elif cmd=="leave":
		client.LeaveChannel(arg)
	else:
		print("unknown command")
	pass;