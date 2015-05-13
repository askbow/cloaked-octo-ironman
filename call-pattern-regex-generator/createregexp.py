#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
A script to generate call patterns ready to be used with CUCM or CUBE.

Inputs:
  phoneranges.csv - a table of all available regional phone number ranges
  must contain such fields as:
   abc    - operator's area code (prefix)
   start  - operator's first number in range
   end    - operator's last number in range
   sp     - operator's name
   region - operator's region (service area)

Outputs:
  numberregexp.csv - a table of regular expressions which cover operator's numbering range

  
Setup:
  Use variables below for settings
'''


# line access, other constant codes:
NUMBER_PREFIX = "98"
# X for CUCM, . for CUBE, \d for standard regexp
ANYDIGIT_SYMBOL = r'X'
# list regions to pick up from source table
LOOKUP_REGION = ("Москва","Москва и Московская область","Московская область")
# number of digits in phone numbers, minus area code and other prefixes' length
PHONEDIGITS = 7

###
###
import csv, time


'''
range_to_pattern adapted from range_regex.py by dimka665 (Dmitry Voronin)
https://github.com/dimka665/range-regex/blob/master/range_regex/range_regex.py
'''
def range_to_pattern(start, stop):
    pattern = ''
    any_digit_count = 0
    for start_digit, stop_digit in zip(str(start), str(stop)):
        if start_digit == stop_digit:
            pattern += start_digit
        elif start_digit != '0' or stop_digit != '9':
            pattern += '[{}-{}]'.format(start_digit, stop_digit)
        else:
            any_digit_count += 1
    if any_digit_count:
        pattern += ANYDIGIT_SYMBOL*any_digit_count 
    return pattern

def phoneregexprocess(DataFileReader):
  operators = dict()
  for line in DataFileReader:
      if line["region"] in LOOKUP_REGION: # only selected regions get processed
        start = int(line['abc'])*10**PHONEDIGITS + int(line['start']) 
        end   = int(line['abc'])*10**PHONEDIGITS + int(line['end'])
        if not line["sp"] in operators:          #   New operator, create first range 
          operators[line["sp"]] = [[start, end]]
          print "#",
        else: # Existing operator
          extended = False
          for ranges in operators[line["sp"]]:
            # difference between the start of range we check and the end of existing range:
            rangediff = (start - ranges[1]) 
            if rangediff == 1:#   Extend existing range
              print "*",
              ranges[1] = end
              extended = True
              break
          if not extended: # if no range was extended after all iterations, append new range
            print "+",
            operators[line["sp"]].append([start, end]) # append new range to operator
  return operators

def main():
  print(time.strftime('[%d/%m %H:%M:%S]',time.localtime())+' Starting')
  DataFileReader = csv.DictReader(open(r'phoneranges.csv'), delimiter=';')
  print(time.strftime('[%d/%m %H:%M:%S]',time.localtime())+' Phone list extracted')
  with open(r'numberregexp.csv','wb') as resultfile:
    fieldnames = ['sp','regexp']
    writer = csv.DictWriter(resultfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    print(time.strftime('[%d/%m %H:%M:%S]',time.localtime())+' Dissecting...')
    operators = phoneregexprocess(DataFileReader) # calling chief worker
    print('\n'+time.strftime('[%d/%m %H:%M:%S]',time.localtime())+' Dissection complete. Generating regex and writing to disk...')
    for operator in operators: #dictionary elements
      for range in operators[operator]:  #lists of lists
        xreg = dict(regexp=NUMBER_PREFIX+range_to_pattern(range[0], range[1]), sp=operator)
        writer.writerow(xreg)
  print('\n'+time.strftime('[%d/%m %H:%M:%S]',time.localtime())+' Done.')  
  
  
if __name__ == '__main__': 
  main()  
  #EOF