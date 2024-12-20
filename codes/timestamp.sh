#!/bin/bash

# not all these steps are stricly necessary to write
# placed here for clarity and ease of reading

current_date=$(date -u +"%Y%m%d%H%M%S")
filename="$current_date.txt"

touch $filename

echo "" >> $filename
echo "" >> $filename
echo "-| $current_date" >> $filename
echo "" >> $filename

nano $filename

