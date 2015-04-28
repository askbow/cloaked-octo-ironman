'''
This is the configexpand.py script.

It is meant to generate config files for switches and routers, 
but can be adapted to generate any iterative config.

Two files are used as input:
 data.csv --- stores iterative parameters, such as names or descriptions
 configtemplate.py --- stores config template from which the resulting config is generated.

One file on output:
 config.conf --- stores the resulting config

'''


import csv, time

# to separate code and data, I load configs from this file:
from configtemplate import *

def configblock(dataline):
  config = CONFIG_TEMPLATE_ITERATIVE
  return config.format(**dataline)

def main():
  print(time.strftime('[%d/%m %H:%M:%S]',time.localtime())+' Starting')
  DataFileReader = csv.DictReader(open(r'data.csv'), delimiter=';')
  print(time.strftime('[%d/%m %H:%M:%S]',time.localtime())+' Parameter list extracted. Generating config...')
  sequence = CONFIG_TEMPLATE_COUNTER['offset'] # offset, if needed
  config = CONFIG_TEMPLATE_ADD_BEFORE + "\n"
  for line in DataFileReader:
    line['sequence'] = str(sequence) # in iterative configs sequence number is often needed
    line.update(CONFIG_TEMPLATE_STATIC)   # that way any static data can be added needed
    sequence = sequence + 1
    config = config + configblock(line)
  config = config + "\n" + CONFIG_TEMPLATE_ADD_AFTER
  print(time.strftime('[%d/%m %H:%M:%S]',time.localtime())+' Config generated. Writing to config.conf ...')
  with open(r'config.conf','wb') as resultfile:
    resultfile.write(config)
  print(time.strftime('[%d/%m %H:%M:%S]',time.localtime())+' Done.')
  
  
  
  
  
if __name__ == '__main__': 
  main()  
  #EOF