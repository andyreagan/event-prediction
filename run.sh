#!/bin/bash

cd /users/a/r/areagan/work/2014/event-prediction

#####################################
## these run all days within one twitter script

# ## we don't have the tweets back then
# # # katrina
# # export EVENTYEAR="2005"
# # export EVENTMONTH="08"
# # export EVENTDAY="29"
# # export MAXDAYS="4"
# # export EVENTNAME="katrina"
# # qsub -V run.qsub

# # boston
# export EVENTYEAR="2013"
# export EVENTMONTH="04"
# export EVENTDAY="15"
# export MAXDAYS="4"
# export EVENTNAME="boston"
# qsub -V run.qsub

# # wedding
# export EVENTYEAR="2011"
# export EVENTMONTH="04"
# export EVENTDAY="29"
# export MAXDAYS="4"
# export EVENTNAME="wedding"
# qsub -V run.qsub

######################################
## this runs each day individually

# boston
export EVENTYEAR="2013"
export EVENTMONTH="04"
export MAXDAYS="0"
export EVENTNAME="boston004"
for DAY in {11..19}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done

# wedding
export EVENTYEAR="2011"
export EVENTMONTH="04"
export MAXDAYS="0"
export EVENTNAME="wedding004"
for DAY in {25..30}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done
export EVENTMONTH="05"
for DAY in {1..3}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done
