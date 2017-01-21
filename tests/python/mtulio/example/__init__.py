import os, sys

dir_current = os.path.dirname(os.path.realpath(__file__))
dir_lib_root = dir_current + '/../../../../python/'
print 'path is :' + dir_lib_root
sys.path.append(dir_lib_root)

#from mtulio.parser.html import messageHelloWorld
import mtulio.parser.html as example
#from mtulio.parser.html.sub import subMessageHelloWorld
#import mtulio.parser.html


print example.messageHelloWorld()

oi = example.ObjectHelloWorld()

print repr(oi)
print oi.returnMessage()

print example.subMessageHelloWorld()

oisub = example.SubClass()
print repr(oisub)
print oisub.returnMessage()
