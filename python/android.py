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

# get prefix
javaProtoPackage = specJSON["javaProtoPackage"]
javaProtoClass = specJSON["javaProtoClass"]

# get apis
apis = specJSON["apis"]

fileC = open("".join([os.getcwd(), "/output/", specJSON["className"], "Provider.java"]), "w")

# prepare for class body
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

# add import

fileC.write("import " + javaProtoPackage + "." + javaProtoClass + ";\n\n")

# class begin
fileC.write("public class " + specJSON["className"] + "Provider\n")
fileC.write("{\n")

# every function
for i in range(0, len(apis)):
    api = apis[i]

    # preload
    responseClass = api["responseClass"]
    if api.has_key("requestClass"):
        requestClass = api["requestClass"]

    # add comment
    fileC.write("\t// " + api["introduction"] + "\n")

    handler = funcHeaderHandler.replace("{JAVA_PROTO_CLASS}", javaProtoClass)
    handler = handler.replace("{RESPONSE_CLASS}", responseClass)
    fileC.write(handler)

    # add func name
    header = funcHeaderName.replace("{API_NAME}", api["apiName"])
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
            if paramType == "str":
                header = header.replace("{PARAM_TYPE}", "String")
            elif paramType == "int":
                header = header.replace("{PARAM_TYPE}", "Integer")
            elif paramType == "uint":
                header = header.replace("{PARAM_TYPE}", "Integer")
            else:
                print "error: can't find type"
            fileC.write(header)
        fileC.write("\n")

    # add request
    if api.has_key("requestClass"):
        header = funcHeaderRequest.replace("{REQUEST_CLASS}", requestClass)
        header = header.replace("{JAVA_PROTO_CLASS}", javaProtoClass)
        fileC.write(header)

    # add response
    header = funcHeaderResponse.replace("{RESPONSE_CLASS}", api["responseClass"])
    header = header.replace("{CLASS_NAME}", specJSON["className"])
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
