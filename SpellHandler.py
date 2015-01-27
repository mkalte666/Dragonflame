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
			e = re.compile('!spell\s+('+client.nick+')\s*\w*')
			match = re.search(e,trailing)
			if match!=None:
				e = re.compile(ur'([\w]*)![\w@.-]*')
				match = re.search(e,prefix)
				if match!=None:
					if client.IsIgnored(match.group(1))!=True:
						if random.randint(0,2)!=0:
							client.SendMessage(params, "!spell "+match.group(1))
						else:
							client.SendMessage(params, random.choice(worddb.generalInsults))