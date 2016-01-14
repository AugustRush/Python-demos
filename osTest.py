#! /usr/bin/env python

import os

#find a crash file from a list files
def findSepecificEctensionFiles(fileList,extension):
	crashes = []
	for f in fileList:
		fileNameSplit = os.path.splitext(f)
		if cmp(fileNameSplit[-1],extension) == 0:
			crashes.append(f)
	if len(crashes) == 0:
		print "this document has not crash files )|||||("
	return crashes

# main method
files = os.listdir("./")
crashFiles = findSepecificEctensionFiles(files,".crash")
parseCrashResult = os.system("./symbolicatecrash ",crashFiles[0],"BaiduInputMethod.dSYM")
print "crashFiles is ",parseCrashResult