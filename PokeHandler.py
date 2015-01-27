import random
import re
import IrcClient
import worddb
import imp
import sys

def HandlerFunc(client, event, prefix, command, params, trailing):
	if params != client.nick:
		if command == "PRIVMSG":
			if trailing.find(client.nick) != -1:
				if trailing.find("poke") != -1 or trailing.find("smack") != -1 or trailing.find("hits") != -1:
					client.SendMessage(params, random.choice(worddb.generalInsults))