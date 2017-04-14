
#!/usr/bin/python

import os
import json

from ios import iosAutoPacker
from android import androidAutoPacker

myGrammarPath = "input/silverGrammar.json"
myInputPath = "input/silverSampleAPI.json"
myOutputJavaPath = "output_java"
myOutputObjcPath = "output_objc"
myProtoName = "Hello"

def makeDirIfNotExist(outputPath):
	if not (os.path.exists(outputPath) and os.path.isdir(outputPath)):
		os.makedirs(os.path.abspath(outputPath))

def doPack():
	ip = iosAutoPacker()
	ip.pack(myGrammarPath, myInputPath, myOutputObjcPath)
	ap = androidAutoPacker()
	ap.pack(myGrammarPath, myInputPath, myOutputJavaPath)

def generateProto(protoName, outputPath, language):
	print "Protobuf File :" + protoName
	currentPath = os.getcwd()
	os.chdir(os.getcwd() + "/input")
	os.system("protoc --" + language + "_out=../" + outputPath + " " + protoName + ".proto")
	os.chdir(currentPath)

def doProtoc(protoName):

	os.system("brew unlink protobuf@2.6")
	os.system("brew link protobuf")

	generateProto(protoName, myOutputObjcPath, "objc")

	os.system("brew unlink protobuf")
	os.system("brew link --force protobuf@2.6")

	generateProto(protoName, myOutputJavaPath, "java")

def main():	
	makeDirIfNotExist(myOutputJavaPath)
	makeDirIfNotExist(myOutputObjcPath)
	doPack()
	doProtoc(myProtoName)

if __name__ == '__main__':
	main()
