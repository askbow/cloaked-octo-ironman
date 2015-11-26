import csv
import time

# We'll remove all fields (coloumns) off the input file, that contain this substring:
LOOKUPSTRING = 'ASCII'

def main():
    print(time.strftime('[%d/%m %H:%M:%S]', time.localtime()) + ' Starting')
    inputReader = csv.DictReader(open(r'input.csv'), delimiter=';')
    # first - a quicker test, if we even hav what we're looking for:
    stringfound = False
    outfield = []
    for field in inputReader.fieldnames:
        if field.find(LOOKUPSTRING) >= 0:
           stringfound = True
        else:
            outfield.append(field)
    if stringfound:
        # Now that we are sure, let's remove tham all, one by one:
        wr = csv.DictWriter(open(r"output.csv", 'wb'), fieldnames=outfield, dialect='excel', delimiter=';')
        wr.writeheader()
        for row in inputReader:
            outrow = {}
            for field in inputReader.fieldnames:
                if field.find(LOOKUPSTRING) < 0:
                    outrow[field] = row[field]
            if outrow != {}:
                wr.writerow(outrow)
    else:
        print(time.strftime('[%d/%m %H:%M:%S]', time.localtime()) + "No fields contain that substring in the input file!")
    print(time.strftime('[%d/%m %H:%M:%S]', time.localtime()) + ' Finished')




if __name__ == '__main__':
    main()
    # EOF
