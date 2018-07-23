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

    FILENAME=$RANDOM.jpg
    gst-launch-1.0 v4l2src num-buffers=1 ! jpegenc ! filesink location=$TARGET/$FILENAME >/dev/null
    python3 ./analysis.py $TARGET/$FILENAME
    echo ""
    echo "* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ *"
    echo ""
done
