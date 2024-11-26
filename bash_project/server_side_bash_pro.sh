#!/bin/bash

file_name=$1
seconds=$2

for second in $(seq 1 $seconds); do
	if [ -e $file_name ]; then
		echo "File $file_name arrived in server after $second seconds"
		exit 0
	fi
	sleep 1
done
echo "Timeout"


