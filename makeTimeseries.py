# look at the happiness of words around an event
#
# USAGE
# python makeTimeseries.py 2009 04 29 1 wedding

# we'll use most of these
from json import loads
import codecs
import time
import gzip
import tarfile

def parser5(infile,freqList,hourCount,keyWords,eventFolder):
  # take in the filename infile, a tgz, and read it
  # check each tweet for some keywords
  # if the keywords are in the tweet, tally that, and save the text
  #   to a file corresponding to it's hour of origin
  
  # got rid of the try loop, keeping fingers crossed for real data
  tar = tarfile.open(infile,'r:gz')
  for member in tar.getmembers():
    # feedback of where this script is
    print member.name
    # grab out the hour.day.month.year
    memberHourDate = member.name[20:-5]
    # check that this is a file (the folder is in the tar)
    if len(memberHourDate) > 0:
      # open corresponding outfile
      g = codecs.open('{0}/tweets/{1}.txt'.format(eventFolder,memberHourDate),'a','utf8')
      f = tar.extractfile(member)
      # try:
      for line in f:
        tweet = loads(line)
        try:
          if tweet['text']:
            for keyWord in keyWords:
              if keyWord in tweet['text']:
                # print 'found a tweet'
                freqList[hourCount+int(memberHourDate[0:2])] += 1
                g.write('{}\n'.format(tweet['text']))
        except:
          # print 'something went wrong'
          pass
      # except:
      #   print 'could not loop over f (or decode line)'
      f.close()
      g.close()
  tar.close()

if __name__ == '__main__':
  # load the things
  from sys import argv
  [year,month,day,buildDays] = map(int,argv[1:5])
  eventName = argv[5]

  # read in more things
  eventFolder = '/users/a/r/areagan/work/2014/event-prediction/events/{}'.format(eventName)
  f = open('{}/keywords.txt'.format(eventFolder))
  keyWords = [line.rstrip() for line in f]
  
  f.close()
  # check these are the right keywords!
  print keyWords
  
  # format date
  import datetime
  date = datetime.datetime(year,month,day)
  date+=datetime.timedelta(days=-buildDays)
  print 'reading {0} for {1} days'.format(eventName,buildDays*2+1)
  
  # build everything
  freqList = [0 for i in range(24*(buildDays*2+1))]
  hourCount = 0
  for i in xrange(buildDays*2+1):
    # the evil monster
    fname = date.strftime('/users/c/d/cdanfort/scratch/twitter/tweet-troll/zipped-raw/%d.%m.%y.tgz')
    print fname
    date+=datetime.timedelta(days=1)
    print 'reading the {}-th file'.format(i+1)
    # do magic
    parser5(fname,freqList,i*24,keyWords,eventFolder)

  # dump this to the screen in case something goes wrong
  print freqList

  ####################################################
  # now we go through the written files, and take the happiness of them
  # no controls for volume yet, just taking the happiness of each hour file

  # use the happiness module that i wrote  
  from storyLab import *
  lens1 = emotionFileReader(0.0)
  lens2 = emotionFileReader(0.5)
  lens3 = emotionFileReader(1.0)
  lens4 = emotionFileReader(max=3.0)
  lens5= emotionFileReader(max=4.0)
  lens6 = emotionFileReader(min=7.0)
  lens7 = emotionFileReader(min=6.0)
  anger = emotionFileReader(fileName='labMT2/anger.txt')
  disgust = emotionFileReader(fileName='labMT2/disgust.txt')
  sadness = emotionFileReader(fileName='labMT2/sadness.txt')
  fear = emotionFileReader(fileName='labMT2/fear.txt')
  surprise = emotionFileReader(fileName='labMT2/surprise.txt')
  happs2 = emotionFileReader(fileName='labMT2/happs.txt')
  # initialize counters and a list of the happiness values
  happsList = [[] for i in range(24*(buildDays*2+1))]
  dateList = ['' for i in range(24*(buildDays*2+1))]
  hourCount = 0
  
  # reset the date
  date = datetime.datetime(year,month,day)
  date+=datetime.timedelta(days=-buildDays)

  # loop over days
  for i in xrange(buildDays*2+1):
    dateString = date.strftime('%d.%m.%y')
    # then hours
    for hour in range(24):
      hourCount+=1
      hourDateString = '{0}.{1}'.format(str(hour),dateString)
      dateList[hourCount-1] = hourDateString
      # open the file and read contents in a big string
      f = open('{0}/tweets/{1:02d}.{2}.txt'.format(eventFolder,hour,dateString),'r')
      tmpStr = f.read()
      f.close()
      
      # evaluate the happiness of that string
      happsList[hourCount-1] = allEmotions(tmpStr,lens1,lens2,lens3,lens4,lens5,lens6,lens7,anger,disgust,sadness,fear,surprise,happs2)

  # write this data to a csv real quick
  f = open('{0}/output.csv'.format(eventFolder),'a')
  for i in range(len(happsList)):
    f.write('{0},{1}'.format(dateList[i],freqList[i]))
    for emotionVal in happsList[i]:
      f.write(',{0}'.format(emotionVal))
    f.write('\n')
  f.close()

  # we hope the see this line
  print 'success'





