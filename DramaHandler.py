# coding=utf-8
import random
import re
import IrcClient
import worddb
import imp
import sys
import textChain

dramaFile = open("drama.txt", 'r')
chain = textChain.parseToChain(dramaFile.read())

def HandlerFunc(client, event, prefix, command, params, trailing):
	if params != client.nick:
		if command == "PRIVMSG":
			e = re.compile('\s*!drama[\w\s]*')
            match = re.search(e,trailing)
			if match!=None:
                client.SendMessage(params, textChain.generateTextFromChain(chain,"",20))
