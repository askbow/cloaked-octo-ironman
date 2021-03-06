#!/usr/bin/python -tt
'''
I did this to understand Erlang calculation.
It is largely based on documentation and examples from www.erlang.com

This algorithm models a time-spread load to predict number of agents (engines, processors, phone lines, call centre operators/agents, etc)
in a queuing system.

'''
import math


def ErlangCPODelayTime(Traffic, Lines, HoldTime, DelayTime):
    Probability = 0
    Probability = ErlangC(Traffic, Lines) *  math.exp(-(Lines - Traffic) * DelayTime / HoldTime)
    if (Probability > 1): 
        return 1
    else:
        # probability that a request will be in queue for time less or equal to
        # DelayTime
        return Probability


def ErlangB(Traffic, pLines):
    # PBR,index;
    if (Traffic > 0):
        PBR = (1 + Traffic) / Traffic
        for index in range(2, pLines + 1):
            PBR = index / Traffic * PBR + 1
        if (PBR > 10000):
            return 0
        return 1 / PBR
    else:
        return 0


def ErlangC(Traffic, pLines):
    # EBResult,Probability
    EBResult = ErlangB(Traffic, pLines)
    Probability = EBResult / (1 - (Traffic / pLines) * (1 - EBResult))
    if (Probability > 1):
        return 1
    else:
        return Probability


def CallDurationCheck(DurationValue):  # mean call duration
    # DurationValue
    if ((DurationValue >= 10) & (DurationValue <= 1200)):
        return DurationValue
    elif (DurationValue < 10):
        return 10
    else:
        return 1200
  
def PercentageCheck(PercentageValue): # % of requests served in due time (without delay), i.e. in AnsweredIn
    if ((PercentageValue>=10) & (PercentageValue<=95)):
        return PercentageValue
    elif (PercentageValue<10):
        return 10
    else:
        return 95

def WrapTimeCheck(WrapTimeValue): #time in seconds
    if ((WrapTimeValue>=0) & (WrapTimeValue<=300)):
        return WrapTimeValue
    elif (WrapTimeValue<0):
        return 0
    else:
        return 300

def CallPerHourCheck(CallsPerHourValue): # call freq in a given hour
    if ((CallsPerHourValue>=10) & (CallsPerHourValue<=5000)):
        return CallsPerHourValue
    elif (CallsPerHourValue<10):
        return 10
    else:
        return 5000
   
def CalculateHour(HourName,CallsPerHourValue,DurationValue,WrapTimeValue,AnsweredIn,PercentageValue):
    # CallsPerHourValue,AgentCounter,AgentBusyTime,AverageDelayAll,ECTraffic,EBTraffic,Lines
    CallsPerHourValue = CallPerHourCheck(CallsPerHourValue)
    AgentBusyTime = CallDurationCheck(DurationValue) + WrapTimeCheck(WrapTimeValue)
    ECTraffic = AgentBusyTime * CallsPerHourValue/3600
    AgentCounter = math.floor(ECTraffic) + 1  
    while (ErlangCPODelayTime(ECTraffic,AgentCounter,AgentBusyTime,AnsweredIn)>(100-PercentageCheck(PercentageValue))/100):  
        AgentCounter+=1  
    AverageDelayAll = math.floor( ErlangC(ECTraffic,AgentCounter) * AgentBusyTime/(AgentCounter-ECTraffic)) + 1
    EBTraffic = CallsPerHourValue * (AverageDelayAll +  CallDurationCheck(DurationValue) )/3600 
    Lines = math.floor(CallDurationCheck(DurationValue) * CallsPerHourValue/3600)+1 
    TrunkBlockingTarget = 0.01 # Trunk blocking target
    # "fraction of the total calls which will be lost because insufficient lines have been provided"
    if (EBTraffic>0):
        while (ErlangB(EBTraffic,Lines)>TrunkBlockingTarget):  
            Lines+=1
    # results:
    Hour = dict()
    Hour['HourName']=HourName # as-is
    Hour['CallsPerHour']=CallsPerHourValue
    Hour['AverageDelayAll']= AverageDelayAll
    Hour['AgentBusyTime']=AgentBusyTime
    Hour['AgentCounter']=AgentCounter
    Hour['Lines']=Lines
    return Hour # dictionary

def PeakResults(HoursData): # all-hours list
    Peak = dict()
    Peak['PeakHourCallsPerHour'] = 0
    Peak['LinesRequired'] = 0
    Peak['MaximumAgents'] = 0
    Peak['PeakHour'] = 0
    for Hour in HoursData:
        Peak['LinesRequired'] =  max(Peak['LinesRequired'],Hour['Lines'])  
        Peak['MaximumAgents'] = max(Peak['MaximumAgents'],Hour['AgentCounter'])  
        PeakHour = max(Peak['PeakHourCallsPerHour'],Hour['CallsPerHour'])
        if PeakHour == Hour['CallsPerHour']:
            Peak['PeakHour']= Hour['HourName']  
    return Peak # dictionary

def main():
    print('Erlang calculation demo')
    DurationValue = 300  # seconds, mean call duration time. 
    '''
    Consider this: http://megamozg.ru/company/rocketcallback/blog/14610/
    Of all calls they've analysed:
    62.25%  - x<1   min
    22.875% - 1<x<3 mins
    12%     - 3<x<5 mins
    06.625% - 5<x   mins
    They also provide a limited industry breakdown of mean call duration.
    '''
    WrapTimeValue = 60   # seconds
    PercentageValue = 80 # % should be served in AnsweredIn
    AnsweredIn = 30      # seconds
    HoursData = []
    print("Input mean number of calls for each hour:")
    for Hour in range(0, 23):
        cph = input("\t"+str(Hour)+":")
        CallsPerHourValue = int(cph)
        HoursData.append(CalculateHour(str(Hour),CallsPerHourValue,DurationValue,WrapTimeValue,AnsweredIn,PercentageValue))
    Peak = PeakResults(HoursData)
    print('Asumptions:\n')
    print(' Mean work duration is', DurationValue, "seconds")
    print(' Server recovery (wrap) time is', WrapTimeValue)
    print(' We expect that', PercentageValue, "of requests are served in",AnsweredIn, "seconds")
    print(' That would require:\n', Peak['LinesRequired'], "queues (connection lines)")
    print(' and a maximum of', Peak['MaximumAgents'], "servers (agents)")
    print(' the peak hour is', Peak['PeakHour'])
    if str(input("Print details? (y/N) "))=="y":
        for Hour in HoursData:
            print('\n\n>Hour: ',Hour['HourName'])
            print('=>Calls Per Hour              ',Hour['CallsPerHour'])
            print('=>Average enqueued Delay      ',Hour['AverageDelayAll'])
            print('=>Mean Agent Busy Time        ',Hour['AgentBusyTime'])
            print('=>Agents Required             ',Hour['AgentCounter'])
            print('=>Lines Required              ',Hour['Lines'])

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
