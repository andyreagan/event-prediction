#!/opt/local/bin/python

import matplotlib.pyplot as plt
import numpy as np
import datetime

def dateSort(listToSort,dates,sortedDates):
  tmp = [listToSort[i] for i in range(len(listToSort))]
  for i in range(len(listToSort)):
    tmp[i] = listToSort[dates.index(sortedDates[i])]
  return tmp

if __name__ == '__main__':
  # get the basics
  from sys import argv
  eventName = argv[1]
  if len(argv)>2:
    plotTitle = argv[2]
  else:
    plotTitle = eventName
  picname = 'figures/{0}.png'.format(eventName)

  # get the data
  f = open('events/{0}/output.csv'.format(eventName),'r')
  rawData = []
  for line in f:
    lineList = line.split(',')
    rawData.append(lineList)

  # sort by time
  timeList = [datetime.datetime(int(x[0].split('.')[3]),int(x[0].split('.')[2]),int(x[0].split('.')[1]),int(x[0].split('.')[0])) for x in rawData]
  timeListSorted = sorted(timeList)
  
  tmpList = [x[1] for x in rawData]
  freqList = dateSort(tmpList,timeList,timeListSorted)
  tmpList = [x[2] for x in rawData]
  happsList = dateSort(tmpList,timeList,timeListSorted)

  # create a figure, fig is now a matplotlib.figure.Figure instance
  fig = plt.figure()
  ax1 = fig.add_axes([0.15,0.2,0.7,0.7]) #  [left, bottom, width, height]          
  
  ax1.plot(range(len(happsList)),happsList,'b')

  ax1.set_xlabel('Time')
  ax1.set_ylabel('Happs')
  # ax1.set_xlim([min(dates)-buffer,max(dates)+buffer]) 
  # ax1.set_ylim([0,24])

  ax1.set_title(plotTitle)
  # plt.xticks([float(i)+0.5 for i in range(4)])
  # plt.yticks([float(i)+0.5 for i in range(3)])
  # ax1.set_xticklabels([1,5,25,50])
  # ax1.set_yticklabels([22,28,35])

  # ax2 = fig.add_axes([0.2,0.2,0.7,0.7]) #  [left, bottom, width, height]          
  ax2 = ax1.twinx()

  ax2.plot(range(len(freqList)),freqList,'r')

  ax2.set_ylabel('Frequency')

  plt.savefig(picname)
  
  plt.close(fig)
