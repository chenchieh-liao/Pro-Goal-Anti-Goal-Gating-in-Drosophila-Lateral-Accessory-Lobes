mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_noExc_connect/10

for w0 in $(seq 1 50)
do 
    python3 control3.py 170 0.01 $w0 &

    wait
    mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_noExc_connect/10/${w0}.png
done


# mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_noExc_connect/30

# for w0 in $(seq 1 50)
# do 
#     python3 control3.py 150 0.01 $w0 &

#     wait
#     mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_noExc_connect/30/${w0}.png

# done


# mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_noExc_connect/90

# for w0 in $(seq 1 50)
# do 
#     python3 control3.py 90 0.01 $w0 &

#     wait
#     mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_noExc_connect/90/${w0}.png

# done

# # 1671079
