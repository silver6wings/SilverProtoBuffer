#!/usr/bin/python

import os
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

if not (os.path.exists("output") and os.path.isdir("output")):
    os.makedirs("output")

jsonFile = open("sample.json", "r")
specJSON = json.loads(jsonFile.read())
jsonFile.close()

providerName = specJSON["providerName"]

# get prefix
iosPrefix = specJSON["iosProtoPrefix"]

# get apis
apis = specJSON["apis"]

fileH = open("".join([os.getcwd(), "/output/", providerName, "+", specJSON["className"],".h"]), "w")
fileM = open("".join([os.getcwd(), "/output/", providerName, "+", specJSON["className"],".m"]), "w")

# class import
fileH.write("\n#import <Foundation/Foundation.h>\n\n")
fileM.write("\n#import \"" + providerName + "+" + specJSON["className"] + ".h\"\n\n")

## todo import protofiles

# class begin
fileH.write("@interface " + providerName + " (" + specJSON["className"] + ")\n\n")
fileM.write("@implementation " + providerName + " (" + specJSON["className"] + ")\n\n")

# prepare for class body
funcHeader = open(os.getcwd() + "/template" + "/iosFuncHeader.txt")
funcHeaderName = funcHeader.readline()
funcHeaderRequest = funcHeader.readline()
funcHeaderParameter = funcHeader.readline()
funcHeader.close()

funcBody = open(os.getcwd() + "/template" + "/iosFuncBody.txt")
funcBodyURL = funcBody.readline()
funcBodyParam = funcBody.readline()
funcBodyRequest = funcBody.read()
funcBody.close()

# every function
for i in range(0, len(apis)):
	api = apis[i]

	# preload
	responseClass = iosPrefix + api["responseClass"]
	if api.has_key("requestClass"):
		requestClass = iosPrefix + api["requestClass"]

	# add comment
	fileH.write("// " + api["introduction"] + "\n")
	fileM.write("// " + api["introduction"] + "\n")

	# add apiName and completion handler
	header = funcHeaderName.replace("{ApiName}", api["apiName"])
	header = header.replace("{responseClass}", responseClass)
	fileH.write(header)
	fileM.write(header)
	nameLength = 8 + len(api["apiName"]) + 14

	# add request
	if api.has_key("requestClass"):
		header = funcHeaderRequest.replace("{requestClass}", requestClass)

		for k in range(0, nameLength - 10):
			fileH.write(" ")
			fileM.write(" ")	

		fileH.write(header)
		fileM.write(header)

	# add parameter
	if (api.has_key("urlParameter")):
		urlParams = api["urlParameter"];

		for paramName in urlParams.keys():
			paramType = urlParams[paramName]
			header = funcHeaderParameter.replace("{ParamName}", paramName[0].upper() + paramName[1:], 1)
			header = header.replace("{ParamName}", paramName, 1)
			if paramType == "str":
				header = header.replace("{ParamType}", "NSString *")
			elif paramType == "int":
				header = header.replace("{ParamType}", "NSInteger")
			elif paramType == "uint":
				header = header.replace("{ParamType}", "NSUInteger")
			else:
				print "error: can't find type"

			for k in range(0, nameLength - 3 - len(paramName)):
				fileH.write(" ")
				fileM.write(" ")	

			fileH.write(header)
			fileM.write(header)		

	# add function body
	fileH.write(";\n")
	fileM.write("{\n")

	# add URL generation
	body = funcBodyURL.replace("{URL}", api["url"])
	body = body.replace("{ProviderName}", providerName)
	fileM.write(body)

	# add URL parameter
	if (api.has_key("urlParameter")):
		urlParams = api["urlParameter"];

		for paramName in urlParams.keys():
			paramType = urlParams[paramName]

			body = funcBodyParam.replace("{ParamName}", paramName)
			if paramType == "str":
				body = body.replace("{ParamPlaceholder}", "%@")
			elif paramType == "int":
				body = body.replace("{ParamPlaceholder}", "%d")
			elif paramType == "uint":
				body = body.replace("{ParamPlaceholder}", "%lu")
			else:
				print "error: can't find type"

			fileM.write(body)

	# add Request method
	body = funcBodyRequest.replace("{Method}", api["method"])
	body = body.replace("{TAG}", api["tag"])
	body = body.replace("{responseClass}", responseClass)

	if api.has_key("requestClass"):
		body = body.replace("{requestExists}", "request")
	else:
		body = body.replace("{requestExists}", "nil")


	fileM.write(body)

	fileM.write("\n}\n\n")

# class end
fileH.write("@end\n")
fileM.write("@end\n")

fileH.close()
fileM.close()
