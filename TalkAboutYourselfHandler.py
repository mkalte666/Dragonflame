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
			e = re.compile('Talk about yourself,{0,1}\s+.*'+client.nick+'.*')
			match = re.search(e,trailing)
			if match!=None:
				e = re.compile(ur'([\w]*)![\w@.-]*')
				match = re.search(e,prefix)
				if match!=None:
					if client.IsIgnored(match.group(1))!=True:
						client.SendMessage(params, random.choice(worddb.greetings)+" "+match.group(1)+"!")
						client.SendMessage(params, "I am a dragon! My creator is mkalte, I'm mostly friendly and if I like you I wont burn you :3")
						client.SendMessage(params, "My DNA is not really good documented, but you can find it here: https://github.com/mkalte666/Dragonflame/ !")