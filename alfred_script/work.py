#! /usr/bin/python
#encoding: utf-8

import TASKs, alfred, json, sys, os

laungh = 'L'
projectX = 'PX'
projectD = 'PD'

def compareStringAB(aStr,bStr):
	return cmp(aStr.lower(),bStr.lower()) == 0


def main(commands):
	if len(commands) == 1:
		if compareStringAB(commands,laungh):
			TASKs.lau()
	elif len(commands) == 3:
		if compareStringAB(commands[0:2],projectD):
			version = int(commands[2])
			TASKs.openProjectDucument(version)
		elif compareStringAB(commands[0:2],projectX):
			version = int(commands[2])
			TASKs.openProjectInXcode(version)		
	else:
		results = []
		countOfCommands = len(commands)
		subtitle = str(countOfCommands)
		item = alfred.Item({'uid': 1, 'arg': commands}, "you should use   'L'   to laungh all work apps.", subtitle.encode('utf-8'))
		results.append(item)
		xml = alfred.xml(results)
		alfred.write(xml)
			
	# if compareStringAB(commands,laungh):
	# 	TASKs.lau()
	# elif compareStringAB(commands,project):
	# 	TASKs.openProject()
	# else:
	# 	results = []
	# 	item = alfred.Item({'uid': 1, 'arg': commands}, "you should use   'L'   to laungh all work apps.", commands.encode('utf-8'))
	# 	results.append(item)
	# 	xml = alfred.xml(results)
	# 	alfred.write(xml)

#excute
if __name__ == "__main__":
    if len(sys.argv) == 1:
       	main(sys.argv)
   	# elif len(sys.argv) == 2:
   	# 	main(sys.argv[1],sys.argv[2])