#!/bin/bash
# Provides a countdown in seconds, multiplied by 5 of the provided input
#Intentionally loops forever until user breaks the process

# Calling my variables
COUNTER=$1
COUNTER=$(( COUNTER * 5 ))

# Function to subtract 1 every second
minusone(){
    COUNTER=$(( COUNTER - 1 ))
    sleep 1
}

# Main Application
# Will perform a loop to reduce counter by one, reporting seconds left
while [ $COUNTER -gt 0 ]
do
    echo "You have $COUNTER seconds left!"
    minusone
done

# Accounting for values of 0 and negative 1
[ $COUNTER = 0 ] && echo "Time is up!" && minusone
[ $COUNTER = "-1" ] && echo "You are late!" && miniusone


# Will perform a loop to reduce COUNTER by one, reporting seconds late
while true
do 
    echo "You are now ${COUNTER#-} seconds late!"
    minusone
done

