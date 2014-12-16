import csv, time 
timetorest = 0.5
timestart = time.time()
print('Opening...')
contactsReader = csv.reader(open(r'c:\bin\pyth\contacts.csv'), delimiter=';')
resultFile = open(r"output.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')
rowrow = []
rowrowrow=[]
rownorow=[]
countone=0
for row in contactsReader:
  countone= countone+1
  rowrow.append(row)
rowrow.pop(0) 
countone= countone-1
print('Contact list extracted.\n\nExpanding...')
if countone>500: timetorest=0.05
if countone>1000: timetorest=0
time.sleep(timetorest) 

for row in rowrow:
  rowrowrow.append(row[0:2])
print('\nThere are '+str(countone)+' records to expand, it may take some time.')
time.sleep(timetorest) 
for row in rowrowrow:
  for rowtwo in rowrow:
    rownorow.append(row+rowtwo)
    if rownorow[-1][0]==rownorow[-1][2]:
	  rownorow.pop()
print('\nExpanded to memory ok.\n\nNow writing output.csv some '+str((countone*countone)-countone)+' records.')
time.sleep(timetorest*2) 
counttwo=0

for row in rownorow:
  if counttwo/countone==counttwo%countone:
    print('.'),
    time.sleep(timetorest/100) 
  wr.writerow(row)
  counttwo= counttwo+1  
print('\nDone expanding '+str(countone)+' records into '+str(counttwo)+' records in ' + str(format(time.time()-timestart-(timetorest*2)-(timetorest/100)*(counttwo/countone), '.2f')) + ' seconds')
