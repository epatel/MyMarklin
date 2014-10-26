#!/bin/bash

while [ 1 ]
do
  ./udpserver.py
  echo RESTARTING SERVER
  sleep 5
done
