#! /usr/bin/python
#encoding: utf-8

import os, StringIO, sys

def lau():
	os.system('open /Applications/Mail.app')
	os.system('open /Applications/百度Hi.app')
	os.system('open /Applications/Xcode.app')


project_6_6_path = '/Users/baidu/BaiduInput/baiduinput_v6_6_0_0_BRANCH/baiduinput_v6_6_0_0_BRANCH'
project_7_0_path = '/Users/baidu/BaiduInput/baiduinput_v7_0_0_0_BRANCH'
project_6_6_XcodeFile = project_6_6_path + '/BaiduInputMethodContainer/'
project_7_0_XcodeFile = project_7_0_path + '/BaiduInputMethodContainer/'
project_Name = 'BaiduInputMethodContainer.xcodeproj/'

def openProjectDucument(version):
	path = ''
	if version == 6:
		path = project_6_6_path
	elif version == 7:
		path = project_7_0_path
	os.chdir(path)
	os.system('open .')


def openProjectInXcode(version):
	filePath = ''
	if version == 6:
		filePath = project_6_6_XcodeFile
	elif version == 7:
		filePath = project_7_0_XcodeFile
	os.chdir(filePath)
	os.system('open ' + project_Name)