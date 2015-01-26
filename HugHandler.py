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
				if trailing.find("hug") != -1:
					client.SendMessage(params, random.choice(worddb.generalYay)+" *hug*")