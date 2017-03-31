#! /usr/bin/python

print 'Hello world'


iosFile = open('iosTemplate.h')

iosContent = iosFile.read()
print iosFile.filename()

if not os.path.exists('iosOutput.h'):
    
