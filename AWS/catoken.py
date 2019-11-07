#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: utf-8 -*-

import CyberArkPythonSDK
import getpass
from subprocess import Popen, PIPE

username = getpass.getuser()
token = CyberArkPythonSDK.client(username=username).get_token()
# token = 'ZjI5N2VkZDMtMWI5Ny00NGE1LTlkNjgtMzczNjkwN2Y1NTJlO0Y3NkQwQjNGRjhBQjcyMzk7MDAwMDAwMDIwRDU0OEI1NDY2Q0U1MTcyRjJFNzNEQTkzRjJEMTkyMkMzQjlDQkZBODkxM0I2MkI2NUJEMkVCQUM0MzVFRjBGMDAwMDAwMDA7'
service = 'cyberark_api_token'

def setpassword(service, password):
    cmd = '/usr/bin/security add-generic-password \
        -U -a {username} -s {service} -w {token} \
        '.format(username=username, service=service, token=token.strip())

    proc = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
    output, err = proc.communicate()
    if err:
      return err
    return None

def getpassword(service):
    cmd = '/usr/bin/security find-generic-password -w -s {service}'.format(service=service)
    proc = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
    output, err = proc.communicate()
    if err:
      return None
    return output

setpassword(service, token)

print("\nTOKEN = " + token)