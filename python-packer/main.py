
#!/usr/bin/python

import os
import json

from ios import iosAutoPacker
from android import androidAutoPacker
from protoc import protoComplier

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

def main():	
	makeDirIfNotExist(myOutputJavaPath)
	makeDirIfNotExist(myOutputObjcPath)
	doPack()

	# protoComplier.doProtocObjc(myProtoName, myOutputObjcPath)
	# protoComplier.doProtocJava(myProtoName, myOutputJavaPath)

if __name__ == '__main__':
	main()
