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
import base64

if __name__ == "__main__":
    msg = ''
    new_string = ''
    replacement = base64.b64encode(bytes('nelley test end '))

    with open("debug/example_1.eml", "r") as raw:
        msg = email.message_from_string(raw.read())
    
    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            old = part.get_payload()
            new_string = str(msg).replace(part.get_payload(), replacement)
            #print new_string

    target = open('eml_save.eml', 'w')
    target.write(new_string)
    target.close()

