#!/bin/bash

while true
do
    echo "=====> ready"
    sleep 1s
    echo "==========> set"
    sleep 1s
    echo "================> cheese!"
    python3 ./camera.py 
    echo "* click *"
    echo "* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ *"
    echo ""
done
