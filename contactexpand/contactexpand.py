import csv
import time


def main():
    timetorest = 0  # no rest for the wicked
    timestart = time.time()
    print(time.strftime('[%d/%m %H:%M:%S]', time.localtime()) + ' Starting')
    contactsReader = csv.reader(open(r'contacts.csv'), delimiter=';')
    resultFile = open(r"output.csv", 'wb')
    global wr, rowrow, rowrowrow, rownorow
    wr = csv.writer(resultFile, dialect='excel')
    rowrow = []
    rowrowrow = []
    rownorow = []
    countone = 0
    for row in contactsReader:
        countone = countone + 1
        rowrow.append(row)
    rowrow.pop(0)
    countone = countone - 1
    print(
        time.strftime(
            '[%d/%m %H:%M:%S]',
            time.localtime()) +
        ' Contact list extracted.\n\nExpanding...')
    for row in rowrow:
        rowrowrow.append(row[2:4])
    for row in rowrowrow:
        for rowtwo in rowrow:
            rownorow.append(row + rowtwo[2:6]) #correction for cisco jabber
            if rownorow[-1][0] == rownorow[-1][2]:
                rownorow.pop()
    print(time.strftime('[%d/%m %H:%M:%S]', time.localtime()) +
          ' Expanded to memory ok. Now writing to output.csv ' +
          str((countone *
               countone) -
              countone) +
          ' records...')
    wr.writerows(rownorow)
    print(time.strftime('[%d/%m %H:%M:%S]', time.localtime()) +
          ' Done expanding ' +
          str(countone) +
          ' records into ' +
          str((countone *
               countone) -
              countone) +
          ' records in ' +
          str(format(time.time() -
                     timestart -
                     (timetorest *
                      2) -
                     (timetorest /
                      100) *
                     ((((countone *
                         countone) -
                        countone)) /
                      countone), '.4f') +
              ' seconds'))

if __name__ == '__main__':
    main()
    # EOF
