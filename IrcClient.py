import socket
import thread 
import time
import Queue
import re
import random

class IrcClient:
	def __init__(self, host, port, nick, realname, printAll=True, isMibbitBot=False):
		self.nick = nick
		self.realname = realname
		self.host = host
		self.port = port
		self.sock = socket.socket()
		self.RecvQueue = Queue.Queue()
		self.SendQueue = Queue.Queue()
		self.printAll = printAll
		self.EventHandlers = []
		
		self.ignoredNicks = []
		
		self.sock.connect((host,port))
		
		thread.start_new_thread(self.ReciveWorker, ())
		thread.start_new_thread(self.SendWorker, ())
		thread.start_new_thread(self.EventWorker, ())
		
		self.RegisterEventHandler(self.PingEventHandler)
		
		self.WaitForSilence()
		self.Send("USER "+self.nick+" 0 * :"+self.realname)
		self.Send("NICK "+self.nick)
		self.WaitForSilence()
	def ReciveWorker(self): 
		recvbuffer = ""
		c = ""
		while True:
			c = self.sock.recv(1)
			if c=='\n':
				if self.printAll == True:
					print("RECV: "+recvbuffer)
				self.RecvQueue.put(recvbuffer)
				recvbuffer = ""
			else:
				recvbuffer += c

	def SendWorker(self):
		while True:
			toSend = self.SendQueue.get()
			if self.printAll == True:
					print("SEND: "+toSend)
			self.sock.send(toSend)
	
	def EventWorker(self):
		while True:
			recvItem = self.RecvQueue.get()
			prefix = ""
			command = ""
			params = ""
			trailing = ""
			expression = re.compile(ur':([\w!.@-]*) {0,1}([A-Za-z0-9]*) {0,1}([\w# ]*) {0,1}:{0,1}(.*)')
			match = re.search(expression, recvItem)
			if match != None:
				prefix = match.group(1)
				command = match.group(2)
				params = match.group(3)
				trailing = match.group(4)
			for func in self.EventHandlers:
				try:
					func(self, recvItem, prefix, command, params, trailing)
				except:
					print("WARNING: Error in handler function!")
					pass
	
	def WaitForSilence(self, maxIterations=10, delay=0.2):
		time.sleep(delay)
		while self.RecvQueue.empty != True:
			time.sleep(delay)
			maxIterations -= 1;
			if maxIterations <= 0:
				break;
			pass;
	
	def RegisterEventHandler(self, func):
		self.EventHandlers.append(func)
	
	def RemoveEventHandler(self, func):
		self.EventHandlers.remove(func)
	
	def Send(self, cmd):
		self.SendQueue.put(cmd+'\n')
	
	def PingEventHandler(self, client, event, prefix, command, params, trailing):
		if event[:4] == "PING":
			self.Send("PONG"+event[4:])				
	
	def SendMessage(self, destination, message):
		self.Send("PRIVMSG "+destination+" :"+message)
	
	def JoinChannel(self, channelname, channelpassword=""):
		self.Send("JOIN "+channelname+" "+channelpassword)
		
	def AddIgnore(self, name):
		self.ignoredNicks.append(name)
	
	def RemoveIgnore(self, name):
		self.ignoredNicks.remove(name)
	
	def IsIgnored(self, name):
		if name in self.ignoredNicks:
			return True
		else:
			return False
