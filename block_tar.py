#!/usr/bin/python2

import os,socket,sys,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",4444))


'''#data will recv drive name
data=s.recvfrom(20)
d_name=data[0]
#data1 will recv drive size
data1=s.recvfrom(20)
d_size=data1[0]
#data2 will recv iqn

data2=s.recvfrom(20)
iqn=data2[0]
#cliaddr will store address of client
cliaddr=data[1][0]
#creating lvm by the name of client drive
os.system('lvcreate --name '+d_name+' --size '+d_size+'M my')
'''
# now time for scsi server configuration
x=os.system('rpm -q scsi-target-utils')
if x==0:
	print "already installed"
else:
	os.system('yum install scsi-target-utils -y')
# making entry in target file
entry="<target iqn.2005-11.exam.com:vini>"+"\n"+"  backing-store /dev/vdd"+"\n"+"</target>"
#appending this var to targets file
f=open('/etc/tgt/targets.conf','a')
f.write(entry)
f.write('\n')
f.close()
# finally  starting  iscsi  service  and service  persistant 
os.system('systemctl   restart  tgtd')

print "done"

