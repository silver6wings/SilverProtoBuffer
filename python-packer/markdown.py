import os
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class docsAutoPacker:

	proto = ""

	def __init__(self):
		return

	def pack(self, protoPath, inputPath, outputPath):
		self.loadProto(protoPath)
		self.loadInput(inputPath)
		self.packToPath(outputPath)

	def loadProto(self, protoPath):
		protoFile = open(protoPath, "r")
		self.proto = protoFile.read()
		protoFile.close()

	def loadInput(self, specPath):
		specFile = open(specPath, "r")
		self.specJSON = json.loads(specFile.read())
		specFile.close()

	def search(self, protoName, protoBase):
		
		protoBase = protoBase.decode('utf-8')		

		protoBody = "message " + protoName

		result = ""

		p = protoBase.index(protoBody) - 1;

		while not protoBase[p] == "{":
			p += 1
			result = result + protoBase[p]
			
		s = 1
		while (s > 0):
			p += 1;
			if protoBase[p] == "{":
				s += 1;
			if protoBase[p] == "}":
				s -= 1;
			result = result + protoBase[p]

		return result

	def packToPath(self, outputPath):

		# prepare parameter
		className = self.specJSON["classOutputName"]
		apis = self.specJSON["apis"]

		# prepare template
		markdownFile = open(os.getcwd() + "/template" + "/markdown.txt")
		markdownTemplate = markdownFile.read()
		markdownFile.close()

		request = "+ Request\n\n```protobuf\n" + "{REQUEST_BODY}\n```\n\n"
		response = "+ Response\n\n```protobuf\n" + "{RESPONSE_BODY}\n```\n\n"

		file = open("".join([os.getcwd(), "/", outputPath, "/", className,".md"]), "w")

		# every function
		for i in range(0, len(apis)):
			api = apis[i]

			markdown = markdownTemplate;
			markdown = markdown.replace("{INTRODUCTION}", api["introduction"])
			markdown = markdown.replace("{URL}", api["url"])
			markdown = markdown.replace("{METHOD}", api["method"])

			markdown = markdown.replace("{INTRODUCTION}", api["introduction"])
			markdown = markdown.replace("{INTRODUCTION}", api["introduction"])

			if api.has_key("introDetail"):
				markdown = markdown.replace("{INTRO_DETAIL}", api["introDetail"] + "\n")
			else:
				markdown = markdown.replace("{INTRO_DETAIL}", "")

			if api.has_key("introLink"):
				markdown = markdown.replace("{INTRO_LINK}", "[API Link](" + api["introLink"] + ")" + "\n")
			else:
				markdown = markdown.replace("{INTRO_LINK}", "")

			if api.has_key("requestClass"):
				body = self.search(api["requestClass"], self.proto)				
				markdown = markdown.replace("{REQUEST_CLASS}", request.replace("{REQUEST_BODY}", body))
			else:
				markdown = markdown.replace("{REQUEST_CLASS}", "")

			if api.has_key("responseClass"):
				body = self.search(api["responseClass"], self.proto)	
				markdown = markdown.replace("{RESPONSE_CLASS}", response.replace("{RESPONSE_BODY}", body))
			else:
				markdown = markdown.replace("{RESPONSE_CLASS}", "")

			file.write(markdown)

		file.close()
