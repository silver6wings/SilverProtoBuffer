#!/usr/bin/python

import os
import json

from ios import iosAutoPacker
from android import androidAutoPacker

def makeDirIfNotExist(outputPath):
	if not (os.path.exists(outputPath) and os.path.isdir(outputPath)):
		os.makedirs(os.path.abspath(outputPath))

def main():	
	myGrammarPath = "input/silverGrammar.json"
	myInputPath = "input/silverSampleAPI.json"
	myOutputPath = "output"

	makeDirIfNotExist(myOutputPath)

	ip = iosAutoPacker()
	ip.pack(myGrammarPath, myInputPath, myOutputPath)

	ap = androidAutoPacker()
	ap.pack(myGrammarPath, myInputPath, myOutputPath)

if __name__ == '__main__':
	main()
