#!/bin/bash

# Create directories for each angle
angles=(180 150 120 90 60 30 0)
for angle in "${angles[@]}"
do
    mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_Exc/$angle
    mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_hfExc/$angle
    mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_ctr/$angle

done

# Loop through each angle and run the processes
for angle in "${angles[@]}"
do
    for w0 in $(seq 1 50)
    do 
        python3 control.py $angle 0.01 $w0 &
        python3 control2.py $angle 0.01 $w0 &
        python3 control3.py $angle 0.01 $w0 &

        wait

        mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_ctr/$angle/${w0}.png
        mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_Exc/$angle/${w0}.png
        mv 3a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2e/data_hfExc/$angle/${w0}.png
    done
done
