#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-

import CyberArkPythonSDK
import pyperclip
import os
from subprocess import Popen, PIPE
​
from os.path import expanduser
home = expanduser("~")
service = 'cyberark_api_token'
​
def getpassword(service):
    cmd = '/usr/bin/security find-generic-password -w -s {service}'.format(service=service)
    proc = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
    output, err = proc.communicate()
    if err:
      return None
    return output
​
token = getpassword(service).strip().decode("utf-8")
# print(getpassword(service).strip().decode("utf-8"))
​
# print(token)
client = CyberArkPythonSDK.client(username="c276669", pretty=True, token=token)
password = client.get_account_value("3939_3")
​
# print(password)
pyperclip.copy(password)