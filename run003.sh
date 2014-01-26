# the few that didn't run from 002


# export EVENTYEAR="2013"
# export MAXDAYS="0"
# export EVENTNAME="mandela001"
# export EVENTMONTH="11"
# for DAY in 30
# do
#   export EVENTDAY=$DAY
#   qsub -V run.qsub
# done



export EVENTYEAR="2012"
export EVENTMONTH="02"
export MAXDAYS="0"
export EVENTNAME="facebookIPO001"
for DAY in 1
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done