
#!/usr/bin/python

import os

class protoComplier:

	@staticmethod
	def doProtocObjc(protoName, outputPath):
		os.system("brew unlink protobuf@2.6")
		os.system("brew link protobuf")
		protoComplier.changeProtoObjcComment(protoName, True)
		protoComplier.generateProto(protoName, outputPath, "objc")

	@staticmethod
	def doProtocJava(protoName, outputPath):
		os.system("brew unlink protobuf")
		os.system("brew link --force protobuf@2.6")
		protoComplier.changeProtoObjcComment(protoName, False)
		protoComplier.generateProto(protoName, outputPath, "java")

	@staticmethod
	def generateProto(protoName, outputPath, language):
		currentPath = os.getcwd()
		os.chdir(os.getcwd() + "/input")
		os.system("protoc --" + language + "_out=../" + outputPath + " " + protoName + ".proto")
		os.chdir(currentPath)
		print "=== Complete " + language + " Protobuf File : " + protoName + " ==="

	@staticmethod
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



