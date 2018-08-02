
# PEACE
[![PEACE LOGO](docs/PEACE.png)](https://youtu.be/Ej8GHj4GGv0)
[**Click here to watch the video!**](https://youtu.be/Ej8GHj4GGv0)

## What is it?
Passenger Emotion Analysis for Commute Enhancement (PEACE) helps fine tune the autonomous vehicle's driving ability through machine learning that detects passenger's faces and runs sentiment analysis on facial expressions. This will be used in autonomous vehicles to for the vehicles to learn about the driving style that riders prefer.


## Project Structure
- PEACE <- main directory
    - App <- directory that contains all of the neccessary modules for the project
    - docs <- directory that contains all of the markdown docs and presentations
    - etc <- directory that contains miscellaneous things like install.sh script
    - sounds <- directory that contains all sounds
    - test_scripts <- sandbox directory for testing things
    - gui.py <- GUI server that listens on port 8082 for a message from analysis.py and display results
    - analysis.py <- server that listens on port 8081 for a message from camera.py and analysis the picture
    - camera.py <- Takes a picture, saves it to ./pics, and sends a message to analysis.py
    - run.sh <- shell script that infinitely calls camera.py

## Environment variables
Variable name | Value
--- | ---
APIKEY | follow [this](https://bit.ly/2Dve8gy) guide to get it
ACCESSKEY | follow [this](https://bit.ly/2NLWzu6) guide to get it
SECRETKEY | follow [this](https://bit.ly/2NLWzu6) guide to get it

## How to run it?

### Step 1: List and Setup of the hardware
- Please refer to hardware documentation [here](docs/hardware.md)

### Step 2: Setup your S3 bucket on AWS to store the pictures
- Please refer to S3 bucket setup documentation [here](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
- Double check that you can access the files in your S3 bucket that you created
- In App/constants.py, set BUCKET_NAME as the Bucket name of the S3 bucket that you just setup.
    - For example, if you created a S3 bucket named "new-bucket", it should be BUCKET_NAME="new-bucket"

### Step 3: Install all dependencies
- Run the install script
```bash
./etc/install.sh
```

### Step 4: Run the servers
- Open up two seperate terminals
- On the first terminal, run the gui.py service. (run with python2)
```bash
python gui.py
```
- On the second terminal, first set the environment variables if you haven't done so
- And run the analysis.py (run with python3)
```bash
export APIKEY="insert_your_ms_azure_face_api_key_here"
export ACCESSKEY="insert_your_aws_access_key_here"
export SECRETKEY="insert_your_aws_secret_key_here"
python3 analysis.py
```
- (you have to run them in this order)
- for getting your FaceAPI key, please go [here](https://azure.microsoft.com/en-us/services/cognitive-services/face/)
- for getting your AWS access and secret keys, please go [here](https://help.bittitan.com/hc/en-us/articles/115008255268-How-do-I-find-my-AWS-Access-Key-and-Secret-Access-Key-)

### Step 5: Run the camera
- There are two ways to run the camera:
- One, you can run it once by directly running the camera.py using python3
```bash
python3 camera.py
```
- Or, you can continuously run it by running the run.sh shell script
```bash
./run.sh
```

## Team members 
Jinwoo Yom, Chaeyoon Lee, Mohannad Ibrahim, Luv Sampat

## Timeline
- 7/06/2018 => Hackathon start date
- 7/07/2018 => Hackathon end date
- 7/26/2018 => Live demo to enter Top 10 Hacks
- 7/27/2018 => Sharktank style pitch in the Executives Board Room

Copyright &copy; 2018 All rights reserved