
#!/usr/bin/python

import os
import json

from ios import iosAutoPacker
from android import androidAutoPacker
from protoc import protoComplier

myGrammarPath = "template/grammar.json"

myInputPath = "input/DemoAPI.json"
myOutputJavaPath = "output_java"
myOutputObjcPath = "output_objc"
myProtoName = "Hello"

def makeDirIfNotExist(outputPath):
	if not (os.path.exists(outputPath) and os.path.isdir(outputPath)):
		os.makedirs(os.path.abspath(outputPath))

def main():	
	makeDirIfNotExist(myOutputJavaPath)
	makeDirIfNotExist(myOutputObjcPath)

	iosAutoPacker().pack(myGrammarPath, myInputPath, myOutputObjcPath)
	androidAutoPacker().pack(myGrammarPath, myInputPath, myOutputJavaPath)

	protoComplier.doProtocObjc(myProtoName, myOutputObjcPath)
	protoComplier.doProtocJava(myProtoName, myOutputJavaPath)

if __name__ == '__main__':
	main()
