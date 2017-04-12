#!/usr/bin/python

import os
import json

from ios import iosAutoPacker
from android import androidAutoPacker

def makeDirIfNotExist(outputPath):
	if not (os.path.exists(outputPath) and os.path.isdir(outputPath)):
		os.makedirs(os.path.abspath(outputPath))

def generateProto(protoName, outputPath, language):
	print "Protobuf File :" + protoName
	currentPath = os.getcwd()
	os.chdir(os.getcwd() + "/input")
	os.system("protoc --" + language + "_out=../" + outputPath + " " + protoName + ".proto")
	os.chdir(currentPath)

def main():	
	myGrammarPath = "input/silverGrammar.json"
	myInputPath = "input/silverSampleAPI.json"

	myOutputJavaPath = "output_java"
	myOutputObjcPath = "output_objc"

	makeDirIfNotExist(myOutputJavaPath)
	makeDirIfNotExist(myOutputObjcPath)

	ip = iosAutoPacker()
	ip.pack(myGrammarPath, myInputPath, myOutputObjcPath)

	ap = androidAutoPacker()
	ap.pack(myGrammarPath, myInputPath, myOutputJavaPath)

	generateProto("silverSampleAPI", myOutputObjcPath, "objc")
	generateProto("silverSampleAPI", myOutputJavaPath, "java")

if __name__ == '__main__':
	main()
