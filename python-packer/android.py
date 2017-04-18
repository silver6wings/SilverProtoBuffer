import os
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class androidAutoPacker:

	grammarJSON = None
	specJSON = None
	platform = "android"

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

	def getStrByType(self, dataTypesDic, dataType):
		if dataTypesDic.has_key(dataType):
			return dataTypesDic[dataType]
		else:
			return "{ERROR: can't find data type in JSON}"

	def packToPath(self, outputPath): 

		providerPackage = self.grammarJSON["providerPackage"]
		providerName = self.grammarJSON["providerName"]
		protoHandler = self.grammarJSON["protoHandler"]
		imports = self.grammarJSON["imports"]
		dataTypes = self.grammarJSON["dataTypes"]

		javaProtoPackage = self.specJSON["javaProtoPackage"]
		javaProtoClass = self.specJSON["javaProtoClass"]

		className = self.specJSON["className"]
		apis = self.specJSON["apis"]
		# prepare template
		funcHeader = open(os.getcwd() + "/template" + "/androidFuncHeader.txt")
		funcHeaderHandler = funcHeader.readline()
		funcHeaderName = funcHeader.readline()
		funcHeaderParameter = funcHeader.readline()
		funcHeaderRequest = funcHeader.readline()
		funcHeaderResponse = funcHeader.readline()
		funcHeader.close()

		funcBody = open(os.getcwd() + "/template" + "/androidFuncBody.txt")
		funcBodyURL = funcBody.readline()
		funcBodyParam = funcBody.readline()
		funcBodyRequest = funcBody.read()
		funcBody.close()

		fileC = open("".join([os.getcwd(), "/", outputPath,"/", className, "Provider.java"]), "w")

		# add import
		fileC.write("package " + providerPackage + ";\n\n")
		fileC.write("import android.content.Context;\n")

		for i in range(0, len(imports)):
			fileC.write("import " + imports[i] + ";\n")
		fileC.write("import " + javaProtoPackage + "." + javaProtoClass + ";\n\n")

		# class begin
		fileC.write("public class " + className + "Provider extends " + providerName + "\n")
		fileC.write("{\n")

		# every handler
		allResponse = [];
		for i in range(0, len(apis)):
			api = apis[i]
			if not api["responseClass"] in allResponse:
				allResponse.append(api["responseClass"]);

		for i in range(0, len(allResponse)):
			handler = funcHeaderHandler.replace("{PROTO_HANDLER}", protoHandler)
			handler = handler.replace("{JAVA_PROTO_CLASS}", javaProtoClass)
			handler = handler.replace("{RESPONSE_CLASS}", allResponse[i])
			fileC.write(handler)
		fileC.write("\n")

		# every function
		for i in range(0, len(apis)):
			api = apis[i]
			apiName = api["api"]

			# preload
			responseClass = api["responseClass"]
			if api.has_key("requestClass"):
				requestClass = api["requestClass"]

			# add comment
			fileC.write("\t// " + api["introduction"] + "\n")

			# add func name
			header = funcHeaderName.replace("{API_NAME}", apiName)
			fileC.write(header)

			# add parameter
			if (api.has_key("urlParameter")):
				urlParams = api["urlParameter"];
				fileC.write("\t\t")
				for paramName in urlParams.keys():
					paramType = urlParams[paramName]
					header = funcHeaderParameter.replace("{PARAM_NAME}", paramName, 1)
					header = header.replace("\n", "")
					header = header.replace("\t", "")
					header = header.replace("{PARAM_NAME}", paramName, 1)
					header = header.replace("{PARAM_TYPE}", self.getStrByType(dataTypes, paramType))

					fileC.write(header)
				fileC.write("\n")

			# add request
			if api.has_key("requestClass"):
				header = funcHeaderRequest.replace("{REQUEST_CLASS}", requestClass)
				header = header.replace("{JAVA_PROTO_CLASS}", javaProtoClass)
				fileC.write(header)

			# add response
			header = funcHeaderResponse.replace("{RESPONSE_CLASS}", api["responseClass"])
			header = header.replace("{CLASS_NAME}", className)
			fileC.write(header)

			fileC.write("\t{\n")

			# add URL generation
			body = funcBodyURL.replace("{URL}", api["url"])
			fileC.write(body)

			# add URL parameter
			if (api.has_key("urlParameter")):
				urlParams = api["urlParameter"];

				for paramName in urlParams.keys():
					body = funcBodyParam.replace("{PARAM_NAME}", paramName)
					fileC.write(body)

			# add Request method
			body = funcBodyRequest.replace("{METHOD}", api["method"])
			body = body.replace("{TAG}", api["tag"])
			body = body.replace("{JAVA_PROTO_CLASS}", javaProtoClass)
			body = body.replace("{RESPONSE_CLASS}", responseClass)

			if api.has_key("requestClass"):
				body = body.replace("{REQUEST_EXISTS}", "requestBody")
			else:
				body = body.replace("{REQUEST_EXISTS}", "null")
			fileC.write(body)

			fileC.write("\t}\n\n")

		# class end
		fileC.write("}\n")
		fileC.close()
		print "Pack Android API Completed!"
