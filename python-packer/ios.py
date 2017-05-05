import os
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class iosAutoPacker:

	grammarJSON = None
	specJSON = None
	platform = "ios"

	def __init__(self):
		return

	def pack(self, grammarPath, inputPath, outputPath):
		self.loadGrammar(grammarPath)
		self.loadInput(inputPath)
		self.packToPath(outputPath)

	def loadGrammar(self, grammarPath):
		grammarFile = open(grammarPath, "r")
		grammarList = json.loads(grammarFile.read())["grammarList"]
		grammarFile.close()
		for i in range(0, len(grammarList)):
			if grammarList[i]["type"] == self.platform:
				self.grammarJSON = grammarList[i]
				break;

	def loadInput(self, specPath):
		specFile = open(specPath, "r")
		self.specJSON = json.loads(specFile.read())
		specFile.close()

	def packToPath(self, outputPath):

		# prepare parameter
		providerName = self.grammarJSON["providerName"]
		dataTypes = self.grammarJSON["dataTypes"]
		dataPlaceHolders = self.grammarJSON["dataPlaceHolders"]
		importsH = self.grammarJSON["importsH"]
		importsM = self.grammarJSON["importsM"]

		className = self.specJSON["classOutputName"]
		iosPrefix = self.specJSON["objcProtoPrefix"]
		iosProto = self.specJSON["objcProtoFile"]
		apis = self.specJSON["apis"]

		# prepare template
		funcHeader = open(os.getcwd() + "/template" + "/iosFuncHeader.txt")
		funcHeaderName = funcHeader.readline()
		funcHeaderCache = funcHeader.readline()
		funcHeaderRequest = funcHeader.readline()
		funcHeaderParameter = funcHeader.readline()
		funcHeader.close()

		funcBody = open(os.getcwd() + "/template" + "/iosFuncBody.txt")
		funcBodyURL = funcBody.readline()
		funcBodyParam = funcBody.readline()
		funcBodyRequest = funcBody.read()
		funcBody.close()

		fileH = open("".join([os.getcwd(), "/", outputPath, "/", providerName, "+", className,".h"]), "w")
		fileM = open("".join([os.getcwd(), "/", outputPath, "/", providerName, "+", className,".m"]), "w")

		# class import
		fileH.write("\n")
		for i in range(0, len(importsH)):
			fileH.write("#import " + importsH[i] + "\n")
		fileH.write("#import \"" + providerName + ".h\"\n")
		fileH.write("#import \"" + iosProto + ".pbobjc.h\"\n")
		fileH.write("\n")

		fileM.write("\n")
		for i in range(0, len(importsM)):
			fileM.write("#import " + importsM[i] + "\n")
		fileM.write("#import \"" + providerName + "+" + className + ".h\"\n")
		fileM.write("\n")

		# class begin
		fileH.write("@interface " + providerName + " (" + className + ")\n\n")
		fileM.write("@implementation " + providerName + " (" + className + ")\n\n")

		# every function
		for i in range(0, len(apis)):
			api = apis[i]
			apiName = api["api"]
			# preload
			responseClass = iosPrefix + api["responseClass"]
			if api.has_key("requestClass"):
				requestClass = iosPrefix + api["requestClass"]

			# add comment
			fileH.write("// " + api["introduction"] + "\n")
			fileM.write("// " + api["introduction"] + "\n")

			# add apiName and completion handler
			header = funcHeaderName.replace("{API_NAME}", apiName)
			header = header.replace("{RESPONSE_CLASS}", responseClass)
			fileH.write(header)
			fileM.write(header)
			nameLength = 8 + len(apiName) + 14

			# add header cache param
			if api.has_key("objcCache"):
				header = funcHeaderCache

				for k in range(0, nameLength - 14):
					fileH.write(" ")
					fileM.write(" ")	

				fileH.write(header)
				fileM.write(header)

			# add header request param
			if api.has_key("requestClass"):
				header = funcHeaderRequest.replace("{REQUEST_CLASS}", requestClass)

				for k in range(0, nameLength - 10):
					fileH.write(" ")
					fileM.write(" ")	

				fileH.write(header)
				fileM.write(header)

			# add header parameter param
			if (api.has_key("urlParameter")):
				urlParams = api["urlParameter"];

				for paramName in urlParams.keys():
					paramType = urlParams[paramName]
					header = funcHeaderParameter.replace("{PARAM_NAME}", paramName[0].upper() + paramName[1:], 1)
					header = header.replace("{PARAM_NAME}", paramName, 1)

					if dataTypes.has_key(paramType):					
						header = header.replace("{PARAM_TYPE}", dataTypes[paramType])					
					else:										
						print "ERROR: can't find data type in JSON"
					
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
			body = body.replace("{PROVIDER_NAME}", providerName)
			fileM.write(body)

			# add URL parameter
			if (api.has_key("urlParameter")):
				urlParams = api["urlParameter"];

				for paramName in urlParams.keys():
					paramType = urlParams[paramName]

					body = funcBodyParam.replace("{PARAM_NAME}", paramName)

					if dataPlaceHolders.has_key(paramType):					
						body = body.replace("{PARAM_PLACEHOLDER}", dataPlaceHolders[paramType])					
					else:										
						print "ERROR: can't find data type in JSON"

					fileM.write(body)

			# add Request method
			body = funcBodyRequest.replace("{METHOD}", api["method"])
			body = body.replace("{TAG}", api["tag"])
			body = body.replace("{RESPONSE_CLASS}", responseClass)

			if api.has_key("requestClass"):
				body = body.replace("{REQUEST_EXISTS}", "request")
			else:
				body = body.replace("{REQUEST_EXISTS}", "nil")


			if api.has_key("objcCache"):
				body = body.replace("{OBJC_CACHE_NEED}", "policy")
			else:
				body = body.replace("{OBJC_CACHE_NEED}", "NSURLRequestUseProtocolCachePolicy")

			fileM.write(body)
			fileM.write("}\n\n")

		# class end
		fileH.write("@end\n")
		fileM.write("@end\n")

		fileH.close()
		fileM.close()
		print "Pack iOS API Completed!"