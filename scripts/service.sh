#!/bin/bash

# Get service name from the first argument
service=$1

# Check if the service is installed
dpkg -l | grep "$service" > /dev/null 2>&1 

# Check the exit code from the dpkg command
if [ $? -ne 0 ]; then
        echo "$service is not installed!"
else
        echo "$service is already installed!"
fi