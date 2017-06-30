#!/usr/bin/python2

import os,socket,sys,time,string,commands

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_ip="192.168.122.200"
s_port=4444
'''drive_name=raw_input("enter name of drive : ")
drive_size=raw_input("enter size in MB : ")

iqn=raw_input("enter iqn : ")
s.sendto(drive_name,(s_ip,s_port))
s.sendto(drive_size,(s_ip,s_port))

s.sendto(iqn,(s_ip,s_port))
'''
print "services loading"


# installing iscsi 
x=os.system('rpm -q iscsi-initiator-utils')
if x==0:
	print "already installed"
else:
	os.system('yum install iscsi-initiator-utils -y')

# sending a discover packet to iscsi target server0
s=commands.getoutput('iscsiadm --mode discoverydb --type sendtargets --portal '+s_ip+' --discover')
print s
# login to target server with received iqn to access the hdd
if ' ' in s:
	l=s.rsplit(' ',1)[0]
	r=s.rsplit(' ',1)[1]
print l
print r
os.system('iscsiadm --mode node --targetname '+r+' --portal '+l+' --login')


