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
#write contents to file
def writeToFile(filePath,contents):
	fileObject = open(filePath,'w')
	with open(filePath,'w') as f:
		f.write(contents)

# main method
os.system("export DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer")
files = os.listdir("./")
crashFiles = findSepecificEctensionFiles(files,".crash")
for crashF in crashFiles:
	commandString = "./symbolicatecrash " + crashF + " BaiduInputMethod.dSYM"
	parseCrashResult = os.popen(commandString).read()
	if len(parseCrashResult) > 0:
		logFileName = os.path.splitext(crashF)[0] + "crash_result_" + ".text"
		createFile = os.system("touch " + logFileName)
		if createFile == 0:
			writeToFile(logFileName,parseCrashResult)
		else:
			print "createFile failed"