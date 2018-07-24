#!/bin/bash

TARGET=./pics

export APIKEY=""
export ACCESSKEY=""
export SECRETKEY=""

while true
do
    echo "=====> ready"
    sleep 1s
    echo "==========> set"
    sleep 1s
    echo "================> cheese!"
    python3 ./camera.py 
    echo ""
    echo "* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ *"
    echo ""
done
