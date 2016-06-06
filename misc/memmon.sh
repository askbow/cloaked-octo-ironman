#!/bin/bash

# MEMMON.sh
# A simple script to log process memory consumption
# Useful to find out which process might be leaking memory.
#
# Mostly based on http://stackoverflow.com/a/147322
# some additions based on http://askubuntu.com/a/383874
# 
# Usage:
# chmod +x memmon.sh
# sudo ./memmon.sh
#
# Sudo: looks like it needs elevated priv. to display ps data on some systems
#
# Let it run for some time, then inspect the produced log.
#

echo "MEM mon script started"
echo $(date)
echo "================================="
while true
do
echo "---------------------------------" >> /tmp/mem_usage
date >> /tmp/mem_usage
ps aux --sort -rss -eo pid,pmem,rss,vsz,comm | head -16 >> /tmp/mem_usage
echo $(date)
# in my case, it's a long-running issue, so need a longer sleep:
sleep 4800
done
