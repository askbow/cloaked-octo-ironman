'''
  A multithread version of contactexpand.py
  It is not very efficient. I made it just to try multithreading in Python.
'''
import csv
from time import localtime, strftime, sleep
import sys
import locale
import threading


class expander(threading.Thread):

    def __init__(self, table, multiplier):
        self.table = table  # table to expand
        self.multiplier = multiplier  # current multiplier
        self.rowinrow = []
        self.rowtow = []
        global rownorow
        threading.Thread.__init__(self)

    def run(self):
        global rownorow
        global wr
        for self.rowtwo in self.table:
            self.rowinrow.append(self.multiplier + self.rowtwo)
            if self.rowinrow[-1][0] == self.rowinrow[-1][2]:
                self.rowinrow.pop()
        wr.writerows(self.rowinrow)
        return True


def main():
    print(strftime('[%d/%m %H:%M:%S]', localtime()) + ' Starting')
    contactsReader = csv.reader(open(r'contacts.csv'), delimiter=';')
    resultFile = open(r'output.csv', 'wb')
    global wr, rowrow, rowrowrow, rownorow
    wr = csv.writer(resultFile, dialect='excel')
    rowrow = []  # holds contacts.csv in usable form
    rowrowrow = []  # holds 'bare' contacts
    rownorow = []  # holds output.csv before writing to disk
    for row in contactsReader:
        rowrow.append(row)
    rowrow.pop(0)
    for row in rowrow:
        rowrowrow.append(row[0:2])
    #print(strftime('[%d/%m %H:%M:%S]',localtime()))
    for row in rowrowrow:
        expander(
            table=rowrow,
            multiplier=row).start()  # run as a separate thread
    #print(strftime('[%d/%m %H:%M:%S]',localtime()))
    print(
        strftime(
            '[%d/%m %H:%M:%S]',
            localtime()) +
        ' Done')  # writing is handled in threads

if __name__ == '__main__':
    main()
   # EOF
