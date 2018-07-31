# -*- coding: utf-8 -*-

# parse eml file

from bs4 import BeautifulSoup
import bs4
import urllib2
import os
import sys
from shutil import copyfile
from datetime import datetime
import email
import pyzmail
import base64
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if __name__ == "__main__":
    msg = ''
    #with open("debug/example_1.eml", "rb") as f:
        #msg = f.read()
        #content = f.readlines()
        #print content
    with open("debug/example_1.eml", "r") as raw:
        msg=pyzmail.PyzMessage.factory(raw)

    #if len(sys.argv)>1:
    #    raw=open(sys.argv[1]).read()

    
    #print 'Subject: %r' % (msg.get_subject(),)
    #print 'From: %r' % (msg.get_address('from'),)
    #print 'To: %r' % (msg.get_addresses('to'),)
    #print 'Cc: %r' % (msg.get_addresses('cc'),)


    #if msg.text_part!=None:
    #    print '-- text --'
    #    print msg.text_part.get_payload()

    if msg.html_part!=None:
        #print '-- html --'
        origin=msg.html_part.get_payload().decode(False)
        print origin
        eml_content=base64.b64encode(bytes(origin))
        #print eml_content
        new_string = string.replace(str(msg), eml_content, 'test')
        #print new_string

        #txt=email.mime.text.MIMEText('The text.', 'plain', 'utf-8')
        #msg.html_part=txt
        #soup = BeautifulSoup(msg.html_part.get_payload(), "html.parser")
        #print 'start'
        #print soup.get_text()

    target = open('eml_save.eml', 'w')
    target.write(new_string)
    target.close()

    #sender=(u'Me', 'me@foo.com')
    #recipients=[(u'Him', 'him@bar.com'), 'just@me.com']
    #subject=u'the subject'
    #text_content=soup.get_text()
    #prefered_encoding='UTF-8'
    #text_encoding='UTF-8'

    #payload, mail_from, rcpt_to, msg_id=pyzmail.compose_mail(\
    #        sender, \
    #        recipients, \
    #        subject, \
    #        prefered_encoding, \
    #        (text_content, prefered_encoding), \
    #        html=None,)
    #        #attachments=[('attached content', 'text', 'plain', 'text.txt', 'us-ascii')])

    #print payload
