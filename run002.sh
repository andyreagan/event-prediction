#!/bin/bash

cd /users/a/r/areagan/work/2014/event-prediction

# export EVENTYEAR="2014"
# export EVENTMONTH="01"
# export MAXDAYS="0"
# export EVENTNAME="bieber_arrested001"
# for DAY in {21..25}
# do
#   export EVENTDAY=$DAY
#   qsub -V run.qsub
# done

export EVENTYEAR="2012"
export EVENTMONTH="02"
export MAXDAYS="0"
export EVENTNAME="facebookIPO001"
for DAY in {1..7}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done
export EVENTMONTH="01"
for DAY in {30..31}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done



export EVENTYEAR="2013"
export EVENTMONTH="09"
export MAXDAYS="0"
export EVENTNAME="kenya_mall_attack001"
for DAY in {17..25}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done




export EVENTYEAR="2013"
export EVENTMONTH="12"
export MAXDAYS="0"
export EVENTNAME="mandela001"
for DAY in {1..8}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done
export EVENTMONTH="11"
for DAY in {30}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done




export EVENTYEAR="2012"
export EVENTMONTH="08"
export MAXDAYS="0"
export EVENTNAME="mars001"
for DAY in {1..5}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done
export EVENTMONTH="07"
for DAY in {28..31}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done





export EVENTYEAR="2013"
export EVENTMONTH="02"
export MAXDAYS="0"
export EVENTNAME="newpope001"
for DAY in {6..14}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done




export EVENTYEAR="2013"
export EVENTMONTH="06"
export MAXDAYS="0"
export EVENTNAME="NSA001"
for DAY in {2..10}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done




export EVENTYEAR="2012"
export EVENTMONTH="11"
export MAXDAYS="0"
export EVENTNAME="obama_election001"
for DAY in {1..9}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done





export EVENTYEAR="2013"
export EVENTMONTH="07"
export MAXDAYS="0"
export EVENTNAME="royalbaby001"
for DAY in {18..26}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done





export EVENTYEAR="2013"
export EVENTMONTH="10"
export MAXDAYS="0"
export EVENTNAME="shutdown001"
for DAY in {1..5}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done
export EVENTMONTH="09"
for DAY in {26..30}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done



export EVENTYEAR="2013"
export EVENTMONTH="04"
export MAXDAYS="0"
export EVENTNAME="thatcher001
for DAY in {5..11}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done




export EVENTYEAR="2013"
export EVENTMONTH="05"
export MAXDAYS="0"
export EVENTNAME="tumblr001
for DAY in {13..21}
do
  export EVENTDAY=$DAY
  qsub -V run.qsub
done