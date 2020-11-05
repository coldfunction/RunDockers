#!/bin/bash

END=$1

#python3 containerCreate.py QQ &

#sleep 10

for i in $(seq 0 $END);
do
        #(time bash bootemplate.sh ${i}) &> time1.${i}.txt &
        #echo "boot template ${i} okok";
	python3 containerCreate.py ${i} &
	python3 calUpcount.py ${i}
#	sleep 10
done


#python3 containerCreate.py 0 &
