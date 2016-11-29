#!/usr/bin/env python

import base64

passfile = open('/home/dotza/python/base/password','r')
passw = passfile.readlines()
passw=base64.b64decode(passw[0].rstrip())

#Initializing ZabbixAPI
from pyzabbix import ZabbixAPI
zapi = ZabbixAPI("http://monitor.st65.ru")
zapi.login("i.kim" , passw )
print "Connected to Zabbix API Version %s" % zapi.api_version()

#Fileread
f1 = open('zabip','r')
iplist = f1.readlines()
f1.close()

#Adding library for every switch model
templat = {'2800-10':'10222','2800-28':'10136','2900-24':'10137','3000-24':'13145','2850-28':'10330','2910-52':'10221'}

for x in range(1, len(iplist)):
#spliting string into list with 3 strings
	ipcomplex = iplist[x].split("\t")
	print ipcomplex[0]
	ip = ipcomplex[0].rstrip()

#Assigning template-ids to modelX variables
	model1 = ipcomplex[1].rstrip()
	print model1
	model2 = ipcomplex[2].rstrip()
	print model2


#Write hostid to variable "hid"
	for h in zapi.hostinterface.get(output="extend", filter={"ip":ip}):
		hid = h['hostid']

#Clear old template, add new template
	zapi.host.update(hostid=hid, templates_clear={"templateid":templat[model1]})
	zapi.host.update(hostid=hid, templates={"templateid":templat[model2]})


#TEMPLATES:
#QTECH QSW2900-24T	=	10137
#QTECH QSW2910-52T	=	10221
#QTECH QSW2800-10T	=	10222
#QTECH QSW2800-28T	=	10136
#QTECH QSW2850-28T	=	10330
#DLINK DGS3000-24T	=	13145
