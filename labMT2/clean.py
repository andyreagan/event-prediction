
for emotion in ['anger','disgust','fear','sadness','happiness','surprise']:
  f = open('labMTResults_{0}.txt'.format(emotion))
  g = open('{0}.txt'.format(emotion),'w')
  for i in range(2000):
    line = f.readline()
    splitLine = line.split('\t')
    g.write(splitLine[0].lstrip('"').rstrip('"'))
    g.write('\t')
    g.write(str(i))
    g.write('\t')
    g.write('{0:5.4f}'.format(float(splitLine[1])))
    g.write('\t')
    g.write('{0:5.4f}'.format(float(splitLine[2])))
    g.write('\n')
