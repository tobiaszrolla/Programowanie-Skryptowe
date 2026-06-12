#!/bin/bash

#!Geting staus and port for validation
demon_status=$(systemctl status vsftpd | grep -oE -m 1 "\([a-z]+\)" | tr -d "()")

if [[ $demon_status != 'running' ]]; then
  echo "demon not running"
  exit -1
fi

#Validating args
if [[ $# -ne 3 ]]; then
  echo "Wrong arg number"
  exit -1
elif [[ ! -d $3 ]]; then
  echo "Neded dir path as secound arg"
  exit -1
fi

usr_name=$1
host=$2
src_path=$3

#enter passwd
echo 'enter password'
read -s password

#making archive backup.tar.gz
tar -czvf backup.tar.gz -C $src_path .

# Call 1. Uses the ftp command with the -inv switches.
#-i turns off interactive prompting.
#-n Restrains FTP from attempting the auto-login feature.
#-v enables verbose and progress.

ftp -inv $host <<EOF
user $usr_name $password
put ./backup.tar.gz
bye
EOF

#removing backup
rm backup.tar.gz
