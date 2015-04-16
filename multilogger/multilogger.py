# -*- coding: utf-8 -*-
'''
This is an example of logging to multiple facilities in python
'''

import logging 


def createmultilogger(name):
 multilog = logging.getLogger(name) # One can put __name__ here for module's name to appear in logs
 multilog.setLevel(logging.DEBUG) #basic level DEBUG INFO WARNING ERROR etc
 # create file handler which logs even debug messages
 fh = logging.FileHandler('/var/log/%s.log',name) # we MUST have WRITE permissions on this file
 fh.setLevel(logging.DEBUG)
 # create console handler with a higher log level - you don't want to flood your console
 ch = logging.StreamHandler()
 ch.setLevel(logging.INFO)
 # create formatter and add it to the handlers
 multilogformatter = logging.Formatter('[%(levelname)s]  %(name)s:[%(asctime)s]:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
 ch.setFormatter(multilogformatter)
 fh.setFormatter(multilogformatter)
 # add the handlers to logger
 multilog.addHandler(ch)
 multilog.addHandler(fh)

#examples
def multilogexample():
 multilog.error('Example error message from multilog')
 multilog.debug('Example debug message from multilog')
 multilog.warning('Example warning message from multilog') 
 multilog.info('Example info message from multilog')

 
 
 
if __name__ == '__main__':
 createmultilogger('multilogger')
 multilogexample()