# coding=utf-8
import random
import re
import IrcClient
import worddb
import imp
import sys
import textChain

literatureFile = open("literature.txt", 'r')
chain = parseToChain(literatureFile.read())

def HandlerFunc(client, event, prefix, command, params, trailing):
	if params != client.nick:
		if command == "PRIVMSG":
			e = re.compile('!literature\s+('+client.nick+')\s*\w*')
                client.SendMessage(params, generateTextFromChain(chain,"",20)