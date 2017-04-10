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

		className = self.specJSON["className"]
		iosPrefix = self.specJSON["iosProtoPrefix"]
		apis = self.specJSON["apis"]

		# prepare template
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

		fileH = open("".join([os.getcwd(), "/", outputPath, "/", providerName, "+", className,".h"]), "w")
		fileM = open("".join([os.getcwd(), "/", outputPath, "/", providerName, "+", className,".m"]), "w")

		# class import
		fileH.write("\n#import <Foundation/Foundation.h>\n\n")
		fileM.write("\n#import \"" + providerName + "+" + className + ".h\"\n\n")

		# class begin
		fileH.write("@interface " + providerName + " (" + className + ")\n\n")
		fileM.write("@implementation " + providerName + " (" + className + ")\n\n")

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

					if dataTypes.has_key(paramType):					
						header = header.replace("{ParamType}", dataTypes[paramType])					
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
			body = body.replace("{ProviderName}", providerName)
			fileM.write(body)

			# add URL parameter
			if (api.has_key("urlParameter")):
				urlParams = api["urlParameter"];

				for paramName in urlParams.keys():
					paramType = urlParams[paramName]

					body = funcBodyParam.replace("{ParamName}", paramName)

					if dataPlaceHolders.has_key(paramType):					
						body = body.replace("{ParamPlaceholder}", dataPlaceHolders[paramType])					
					else:										
						print "ERROR: can't find data type in JSON"

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
