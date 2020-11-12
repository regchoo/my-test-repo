#!/bin/bash

for ((x=1;x<10000000000;x++))
	do printf "%010d\n" $x
done > evilfile.txt
