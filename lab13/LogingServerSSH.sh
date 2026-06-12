#!/bin/bash

#!Geting staus and port for validation
demon_status=$(systemctl status sshd | grep -oE -m 1 "\([a-z]+\)" | tr -d "()")
port=$(systemctl status sshd | grep -oE -m1 "port [0-9]+." | tr -d 'a-z.')

if [[ $demon_status != 'running' ]]; then
  echo "demon not running"
  exit -1
fi
if [[ $port -ne 22 ]]; then
  echo "Wrong port nr"
  exit -1
fi

#! Geting imupt validation
if [[ $# -ne 1 ]]; then
  echo "Wrong arg number"
  exit -1
fi

#! conect to remot host list files and active processes
remout_host=$1
ssh $remout_host "ls -la .&& ps aux" >output.txt
