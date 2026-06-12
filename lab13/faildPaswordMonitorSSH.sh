#!/bin/bash

# Checking if distro and log file existance
file='path'
if [[ -f /var/log/secure ]]; then
  echo "Executed on RH based distro"
  file='/var/log/secure'
elif [[ -f /var/log/auth.log ]]; then
  echo "Executed on Debian based distro"
  file='/var/log/auth.log'
else
  echo "Can not find log file"
  exit -1
fi
#Checking read perm
if [[ ! -r $file ]]; then
  echo "Dosent have a permision to read"
  exit -1
fi

echo 'press q to stop'
#Log count
LOG_NR=$(cat $file | grep -cE 'ssh.+Failed password')

while true; do
  #Counting and compering wrong pass
  log_count=$(cat $file | grep -cE 'ssh.+Failed password')
  if [[ $log_count -ne $LOG_NR ]]; then
    echo 'Warning wrong password'
    cat $file | grep -E 'ssh.+Failed password' >./raport
  fi

  #Exiting
  read -st 2 -n 1 key
  if [[ $key == 'q' ]]; then
    echo 'Stoping'
    break
  fi
done
