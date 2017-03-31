#!/usr/bin/python

import os
import json

if not (os.path.exists("output") and os.path.isdir("output")):
    os.makedirs("output")


jsonFile = open("sample.json", "r")
specJSON = json.loads(jsonFile.read())
jsonFile.close()

iosPrefix = specJSON["iosProtoPrefix"]

apis = specJSON["apis"]

providerName = specJSON["providerName"]

iosFileH = open("".join([os.getcwd(), "/output/", providerName, "+", specJSON["providerName"],".h"]), "w")
iosFileM = open("".join([os.getcwd(), "/output/", providerName, "+", specJSON["providerName"],".m"]), "w")

# class import
iosFileH.write("\n#import <Foundation/Foundation.h>\n\n")
iosFileM.write("\n#import \"" + providerName + "+" + specJSON["className"] + ".h\"\n\n")

## todo import protofiles

# class begin
iosFileH.write("@interface " + providerName + " (" + specJSON["className"] + ")\n\n")
iosFileM.write("@implementation " + providerName + " (" + specJSON["className"] + ")\n\n")

# class body
iosFuncHeader = open(os.getcwd() + "/iosTemplate/" + "funcHeader.txt")
iosFuncHeaderName = iosFuncHeader.readline()
iosFuncHeaderRequest = iosFuncHeader.readline()
iosFuncHeaderParameter = iosFuncHeader.readline()
iosFuncHeader.close()

iosFuncBody = open(os.getcwd() + "/iosTemplate/" + "funcBody.txt")
iosFuncBodyURL = iosFuncBody.readline()
iosFuncBodyParam = iosFuncBody.readline()
iosFuncBodyRequest = iosFuncBody.read()
iosFuncBody.close()

# every function
for i in range(0, len(apis)):
	api = apis[i]

	if api.has_key("requestClass"):
		requestClass = iosPrefix + api["requestClass"]

	responseClass = iosPrefix + api["responseClass"]

	# add comment

	iosFileH.write("// " + api["introduction"] + "\n")
	iosFileM.write("// " + api["introduction"] + "\n")

	# add apiName and completion handler
	header = iosFuncHeaderName.replace("{ApiName}", api["apiName"])
	header = header.replace("{responseClass}", responseClass)
	iosFileH.write(header)
	iosFileM.write(header)
	nameLength = 8 + len(api["apiName"]) + 14

	# add request
	if api.has_key("requestClass"):
		header = iosFuncHeaderRequest.replace("{requestClass}", requestClass)

		for k in range(0, nameLength - 10):
			iosFileH.write(" ")
			iosFileM.write(" ")	

		iosFileH.write(header)
		iosFileM.write(header)

	# add parameter
	if (api.has_key("urlParameter")):
		urlParams = api["urlParameter"];

		for paramName in urlParams.keys():
			paramType = urlParams[paramName]
			header = iosFuncHeaderParameter.replace("{ParamName}", paramName[0].upper() + paramName[1:], 1)
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
				iosFileH.write(" ")
				iosFileM.write(" ")	

			iosFileH.write(header)
			iosFileM.write(header)		

	# add function body
	iosFileH.write(";\n")
	iosFileM.write("{\n")

	# add URL generation
	body = iosFuncBodyURL.replace("{URL}", api["url"])
	body = body.replace("{ProviderName}", providerName)
	iosFileM.write(body)

	# add URL parameter
	if (api.has_key("urlParameter")):
		urlParams = api["urlParameter"];

		for paramName in urlParams.keys():
			paramType = urlParams[paramName]
			body = iosFuncBodyParam.replace("{ParamName}", paramName)
			if paramType == "str":
				body = body.replace("{ParamPlaceholder}", "%@")
			elif paramType == "int":
				body = body.replace("{ParamPlaceholder}", "%d")
			elif paramType == "uint":
				body = body.replace("{ParamPlaceholder}", "%lu")
			else:
				print "error: can't find type"

			iosFileM.write(body)

	# add Request method
	body = iosFuncBodyRequest.replace("{Method}", api["method"])
	body = body.replace("{TAG}", api["tag"])

	if api.has_key("requestClass"):
		body = body.replace("{requestExists}", "request")
	else:
		body = body.replace("{requestExists}", "nil")

	body = body.replace("{responseClass}", responseClass)

	iosFileM.write(body)

	iosFileM.write("\n}\n\n")

# class end
iosFileH.write("@end\n")
iosFileM.write("@end\n")

iosFileH.close()
iosFileM.close()
