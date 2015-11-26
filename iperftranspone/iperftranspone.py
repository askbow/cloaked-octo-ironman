import csv
import time


def main():
    print(time.strftime('[%d/%m %H:%M:%S]', time.localtime()) + ' Starting')
    inputFile = open(r'iperf-extracted-timeseries.csv')
    reader = csv.DictReader(inputFile, delimiter=';')
    result = list()
    fieldnames = ['time',]
    for row in reader:
        resultUpdated = False
        if result == []:
            result.append({'time':row['time'], row['id']:row['data']})
            resultUpdated = True
        for moment in result:
            if moment['time'] == row['time']:
                moment[row['id']] = row['data']
                resultUpdated = True
        if not resultUpdated:
            result.append({'time':row['time'], row['id']:row['data']})
            resultUpdated = True
        if  not row['id'] in fieldnames: fieldnames.append(row['id'])  
    print(time.strftime('[%d/%m %H:%M:%S]', time.localtime()) + ' Done data extraction, writing to disk...')    
        
    resultFile = open(r"iperf-transposed-timeseries.csv", 'wb')
    wr = csv.DictWriter(resultFile, dialect='excel', fieldnames=fieldnames, delimiter=';')
    wr.writeheader()
    for row in result:
        wr.writerow(row)
    #cleaning up:
    inputFile.close()
    resultFile.close()
    print(time.strftime('[%d/%m %H:%M:%S]', time.localtime()) + ' Finished.')



if __name__ == '__main__':
    main()
    # EOF
