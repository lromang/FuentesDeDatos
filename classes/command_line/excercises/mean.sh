#! /bin/bash

read N
sum=0
for i in `seq $N`
do
read n
sum=$(($sum + $n))
done
printf "%.3f" $(echo $sum/$N | bc -l)
