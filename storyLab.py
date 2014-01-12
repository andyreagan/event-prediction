#!/usr/bin/python
#
# storyLab.py
#
# a python module for using the labMT1.0 dataset
# no dependencies, unless using the plot function
#  (then we use matplotlib)
#
# USAGE
#
# In python:
#   tmpstr = 'a happy sentence'
#   from storyLab import emotionFileReader
#   lens = emotionFileReader(0.0)
#   from storyLab import emotion
#   happs = emotion(tmpstr,lens)
#
# In a shell:
#   alias happiness="$(pwd)/storyLab.py"
#   cat storyLab.py | happiness
#   storyLab.py happiness
#
# written by Andy Reagan
# 2014-01-12

def emotionFileReader(stopval=0.0,fileName='labMT1.txt',min=1.0,max=9.0):
  ## stopval is our lens, \Delta h
  ## read the labMT dataset into a dict with this lens
  ## must be tab-deliminated, emotion value as third tab
  f = open(fileName,'r')
  tmpDict = dict([(line.split('\t')[0],[x.rstrip() for x in line.split('\t')[1:]]) for line in f])
  f.close()
  ## remove words
  stopWords = []
  for word in tmpDict:
    if abs(float(tmpDict[word][1])-5.0) < stopval:
      stopWords.append(word)
    else:
      if float(tmpDict[word][1]) < min:
        stopWords.append(word)
      else:
        if float(tmpDict[word][1]) > max:
          stopWords.append(word)
  
  for word in stopWords:
    del tmpDict[word]

  return tmpDict

def emotion(tmpStr,someDict):
  score_list = []
  # doing this without the NLTK
  words = [x.lower().lstrip("?';:.$%&()\\!*[]{}|\"<>,^-_=+").rstrip("@#?';:.$%&()\\!*[]{}|\"<>,^-_=+") for x in tmpStr.split()]
  for word in words:
    if word in someDict:
      score_list.append(float(someDict[word][1]))

  ## with numpy (and mean in the namespace)
  ## happs = mean(score_list)
  
  ## without numpy
  if len(score_list) > 0:
    happs = sum(score_list)/float(len(score_list))
  else:
    happs = 0

  return happs

def allEmotions(tmpStr,*allDicts):
  emotionList = []
  for tmpDict in allDicts:
    emotionList.append(emotion(tmpStr,tmpDict))
  return emotionList

def plothapps(happsTimeSeries,picname):
  ## uses matplotlib
  import matplotlib.pyplot as plt

  ## create a figure, fig is now a matplotlib.figure.Figure instance
  fig = plt.figure()

  ## plot the time series
  ax1 = fig.add_axes([0.2,0.2,0.7,0.7]) ##  [left, bottom, width, height]
  ax1.plot(range(len(happs)),happsTimeSeries)
  ax1.set_xlabel('Time')
  ax1.set_ylabel('Happs')
  ax1.set_title('Happiness over time')

  plt.savefig(picname)
  plt.close(fig)

if __name__ == '__main__':
  ## run from standard in
  import fileinput
  labMT = emotionFileReader(0.0)
  happsList = [emotion(line,labMT) for line in fileinput.input()]
  
  for value in happsList:
    print value
    
  


