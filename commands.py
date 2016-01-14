#! /usr/bin/env python

import os

lsValue = os.popen("ls")
print "lsValue is ",lsValue
success = os.system("touch test.text")
if success == 0:
	os.system("ls >> test.text")