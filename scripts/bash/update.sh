#!/bin/bash

swaymsg -t get_outputs | grep focused > /tmp/outputs_inf

f_o1=$(sed -n '1p' /tmp/outputs_inf | cut -c 16-19)
f_o2=$(sed -n '2p' /tmp/outputs_inf | cut -c 16-19)
len=0

if [[ $f_o1 == 'true' ]]
then
  len=185
else
  len=138
fi

for i in $(seq 1 $len);
do
  echo "=" | tr -d '\n'
done

for i in $(seq 1 $len);
do
  if [[ $len == 185 ]]
  then
    if [[ $i == 91 ]]
    then
      echo "PACMAN" | tr -d '\n'
    else
      echo "=" | tr -d '\n'
    fi
  else
    if [[ $i == 62 ]]
    then
      echo "PACMAN" | tr -d '\n'
    else
      echo "=" | tr -d '\n'
    fi
  fi
done

if [[ $len == 185 ]]
then
  for i in $(seq 1 195);
  do 
    echo "=" | tr -d '\n'
  done
else
  for i in $(seq 1 124);
  do
    echo "=" | tr -d '\n'
  done
fi

sudo pacman --noconfirm -Syu 

if [[ $f_o1 == 'true' ]]
then
  len=186
else
  len=139
fi

for i in $(seq 1 $len);
do
  echo "=" | tr -d '\n'
done

for i in $(seq 1 $len);
do
  if [[ $len == 186 ]]
  then
    if [[ $i == 91 ]]
    then
      echo "PARU" | tr -d '\n'
    else
      echo "=" | tr -d '\n'
    fi
  else
    if [[ $i == 62 ]]
    then
      echo "PARU" | tr -d '\n'
    else
      echo "=" | tr -d '\n'
    fi
  fi
done

if [[ $len == 186 ]]
then
  for i in $(seq 1 195);
  do 
    echo "=" | tr -d '\n'
  done
else
  for i in $(seq 1 124);
  do
    echo "=" | tr -d '\n'
  done
fi

paru --noconfirm -Syu 
echo "We are up to date right now!!!"
