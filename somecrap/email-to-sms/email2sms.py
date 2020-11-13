#!/usr/bin/env python

# convert emails from postfix
# to a format suitable for
# smstools3 to send out
# via SMS


import email.parser
import sys
import string
import random
import os
import pwd
import grp

full_msg = sys.stdin.readlines()
msg = email.message_from_string(''.join(full_msg));
ranext = (''.join(random.choice(string.ascii_lowercase) for i in range(9)))
encode_type = msg['Content-Transfer-Encoding']

# debug incoming email
#incomingmail = open("/work/incomingmail.txt", 'w')
#print >> incomingmail, msg
#incomingmail.close()

sms_file = open("/var/spool/sms/outgoing/sms."+ranext, 'w')

print >> sms_file, "To:",msg['to'].split('@')[0][-10:]
print >> sms_file, "\nSubject:",msg['subject']
print >> sms_file, "Date:",msg['date']
if encode_type == "base64":
    print >> sms_file, "\n",msg.get_payload(decode=True)
else:
    print >> sms_file, "\n",msg.get_payload()

sms_file.close()

path = "/var/spool/sms/outgoing"
for root, dirs, files in os.walk(path):
    for eachfile in files:
	fname = os.path.join(root, eachfile)
	os.chown(fname, pwd.getpwnam("smsd").pw_uid, grp.getgrnam("smsd").gr_gid)
