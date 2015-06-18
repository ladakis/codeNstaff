#!/bin/sh

# @author: ladakis
# version: over 9000

# A script that ejects and injects the cdrom as many times as the hour. Just 
# like a clock. :)

# I was board to search the man page for crafting the format in date. 
# awk does the work so... who cares?

hour=`date |awk '{print $4}' | awk -F\: '{print $1}'`
for i in `seq 1 $hour`
do
	echo $i from $hour
	eject
	sleep 1
	eject -t
	sleep 1
done
