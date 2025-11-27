#!/bin/bash

# this script restarts an ec2 instance periodically to cycle ip
# addresses and evade instagram blacklisting ips
# note: aws cli authenticated sessions last only 12 hours

INSTANCEID="i-magicalawsnumber"

function start {
    aws ec2 start-instances --instance-id $INSTANCEID > /dev/null 2>&1 && echo "started instance"
}

function stop {
    aws ec2 stop-instances --instance-id $INSTANCEID > /dev/null 2>&1 && echo "stopped instance"
}

while true;
do
    start && sleep 70 && stop
    sleep 5
done

