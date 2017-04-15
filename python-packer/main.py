
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

def changeProtoObjcComment(protoName, needObjcPrefix):
	protoFile = open(os.getcwd() + "/input/" + protoName + ".proto", "r");
	protoContent = protoFile.read()
	protoFile.close()

	protoContent = protoContent.replace("// option objc_class_prefix", "option objc_class_prefix");
	if not needObjcPrefix:	
		protoContent = protoContent.replace("option objc_class_prefix", "// option objc_class_prefix");	

	protoFile = open(os.getcwd() + "/input/" + protoName + ".proto", "w");
	protoFile.write(protoContent)
	protoFile.close()

def doProtocObjc(protoName):
	os.system("brew unlink protobuf@2.6")
	os.system("brew link protobuf")
	changeProtoObjcComment(protoName, True)
	generateProto(protoName, myOutputObjcPath, "objc")

def doProtocJava(protoName):
	os.system("brew unlink protobuf")
	os.system("brew link --force protobuf@2.6")
	changeProtoObjcComment(protoName, False)
	generateProto(protoName, myOutputJavaPath, "java")

def main():	
	makeDirIfNotExist(myOutputJavaPath)
	makeDirIfNotExist(myOutputObjcPath)
	doPack()
	doProtocObjc(myProtoName)
	doProtocJava(myProtoName)

if __name__ == '__main__':
	main()
