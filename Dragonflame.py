#!/usr/bin/python3
import random
import re
import IrcClient
import worddb
import imp
import sys
	
client = IrcClient.IrcClient("irc.mibbit.net", 6667, "Dragonflame", "DragonBot@invalid", False, True)
client.JoinChannel("#exploders")
client.SendMessage("#exploders", "*yawns* hello people")
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

while True:
	cmd = ""
	arg = ""
	inCmd = raw_input("CMD?: ")
	e = re.compile(ur'(\w*)\s*(\w*)')
	match = re.search(e, inCmd)
	cmd=match.group(1)
	arg = match.group(2)
	
	if cmd=="reload":
		ReloadModule(arg)
	elif cmd=="load":
		LoadModule(arg)
			
	elif cmd=="exit" or cmd=="kill" or cmd=="quit":
		exit()
	else:
		print("unknown command")
	pass;