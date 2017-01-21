import os, sys

# Add a custom lib to python path
dir_current = os.path.dirname(os.path.realpath(__file__))
dir_lib_root = dir_current + '/../../../../python/'
print 'path is :' + dir_lib_root
sys.path.append(dir_lib_root)

#########################
# Setting alias for a lib
import mtulio.example as example

print "[mtulio.example] as> Calling method from lib mtulio.example : " + example.messageHelloWorld()

helloObject = example.ObjectHelloWorld()
print "[mtulio.example] as> Representation of object in lib mtulio.example : " + repr(helloObject)
print "[mtulio.example] as> Method of Object lib mtulio.example : " + helloObject.returnMessage()

# Sub file from path mtulio.example
print "[mtulio.example.sub] as> Calling method from sub lib mtulio.example : " + example.subMessageHelloWorld()

helloObjectSub = example.SubClass()
print "[mtulio.example.sub] as> Representation of Sub Object in lib mtulio.example : " + repr(helloObjectSub)
print "[mtulio.example.sub] as> Method of Sub Object lib mtulio.example : " + helloObjectSub.returnMessage()

#################################################
# Importing specific functions
from mtulio.example import messageHelloWorld

print "[mtulio.example] import> Calling method directly from lib mtulio.example : " + messageHelloWorld()

from mtulio.example import subMessageHelloWorld
print "[mtulio.example.sub] import> Calling method directly from lib mtulio.example : " + subMessageHelloWorld()

# Importing specific Objects
from mtulio.example import ObjectHelloWorld

helloworld_import = ObjectHelloWorld()
print "[mtulio.example] import> Instancing objects directly from lib mtulio.example : " + helloworld_import.returnMessage()

from mtulio.example import SubClass

helloworldsub_import = SubClass()
print "[mtulio.example.sub] import> Instancing objects directly from lib mtulio.example : " + helloworldsub_import.returnMessage()
