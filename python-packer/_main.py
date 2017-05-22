
#!/usr/bin/python

import os
import json

from ios import iosAutoPacker
from android import androidAutoPacker
from markdown import docsAutoPacker
from protoc import protoComplier

myGrammarPath = "template/grammar.json"

myInputPath = "input/DemoAPI.json"
myOutputDocsPath = "output_docs"
myOutputJavaPath = "output_java"
myOutputObjcPath = "output_objc"
myProtoName = "Hello"

def makeDirIfNotExist(outputPath):
	if not (os.path.exists(outputPath) and os.path.isdir(outputPath)):
		os.makedirs(os.path.abspath(outputPath))

def main():	

	makeDirIfNotExist(myOutputObjcPath)
	iosAutoPacker().pack(myGrammarPath, myInputPath, myOutputObjcPath)
	protoComplier.doProtocObjc(myProtoName, myOutputObjcPath)

	makeDirIfNotExist(myOutputJavaPath)
	androidAutoPacker().pack(myGrammarPath, myInputPath, myOutputJavaPath)
	protoComplier.doProtocJava(myProtoName, myOutputJavaPath)

	makeDirIfNotExist(myOutputDocsPath)
	docsAutoPacker().pack("input/Hello.proto", "input/DemoAPI.json", myOutputDocsPath)

if __name__ == '__main__':
	main()
