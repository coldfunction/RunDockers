#!/bin/bash

END=$1

#python3 containerCreate.py QQ &

#sleep 10
i=0
num=0
#for i in $(seq 0 $END);
while [ $num != $1 ]
do
        #(time bash bootemplate.sh ${i}) &> time1.${i}.txt &
        #echo "boot template ${i} okok";
	python3 containerCreate.py ${i} &
	#python3 calUpcount.py ${i}
        num=$(python3 calUpcount-nocheck.py)
        i=$(($i+1))
#	sleep 10
done


#python3 containerCreate.py 0 &
