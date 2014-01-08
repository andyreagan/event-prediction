#!/bin/bash

cd /users/a/r/areagan/work/2014/event-prediction

# katrina
export EVENTYEAR="2005"
export EVENTMONTH="08"
export EVENTDAY="29"
export MAXDAYS="4"
export EVENTNAME="katrina"
qsub -V run.qsub

# boston
export EVENTYEAR="2013"
export EVENTMONTH="04"
export EVENTDAY="15"
export MAXDAYS="4"
export EVENTNAME="boston"
qsub -V run.qsub

# wedding
export EVENTYEAR="2011"
export EVENTMONTH="04"
export EVENTDAY="29"
export MAXDAYS="4"
export EVENTNAME="wedding"
qsub -V run.qsub
