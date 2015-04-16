'''
This is an example of how to generate a simple session number to track application flows
(for example, for logging)
'''
from time import time
from os import urandom 
from hashlib import md5

# use Python 3 print function
# this allows this code to run on python 2.x and 3.x
from __future__ import print_function


def sessiongen():
 # We will use a 4-byte urandom number concatenated with microsecond-precision local time to identify each session in logs:
 sesstimemiltm = int(round(time()*1000000))
 sessrndid = str(int(urandom(4).encode('hex'), 16))
 return str(int(sesstimemiltm))+sessrndid
 

'''
This one is useful when there is some data to salt
Good input examples:
- client IP
- username
- request string (might be not so good)
'''
def sessiongendigest(input):
 return md5('input'+sessiongen()).hexdigest() 

#this one combines the two approaches:
def sessiongenfull(input):
 return sessiongen()+sessiongendigest(input)  
 
def main():
 print('sessiongen():  ',sessiongen())
 print('sessiongendigest("SPAM"):  ',sessiongendigest('SPAM'))
 print('sessiongenfull("EGGS"):  ',sessiongenfull('EGGS')) 

 
 
 
if __name__ == '__main__':
 main()