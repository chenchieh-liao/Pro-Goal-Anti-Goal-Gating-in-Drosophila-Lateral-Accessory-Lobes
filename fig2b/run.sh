# mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_no101418/45
# mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/45

# for w0 in $(seq 1 50)
# do 
#     python3 control.py 135 0.01 $w0 &
#     python3 control2.py 135 0.01 $w0 &
#     wait
#     mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/45/${w0}.png
#     mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_no101418/45/${w0}.png
# done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_no101418/60
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/60

for w0 in $(seq 1 50)
do 
    python3 control.py 120 0.01 $w0 &
    python3 control2.py 120 0.01 $w0 &
    wait
    mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/60/${w0}.png
    mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_no101418/60/${w0}.png
done

# mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_no101418/75
# mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/75

# for w0 in $(seq 1 50)
# do 
#     python3 control.py 105 0.01 $w0 &
#     python3 control2.py 105 0.01 $w0 &
#     wait
#     mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_ctr/75/${w0}.png
#     mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2b/data_no101418/75/${w0}.png
# done

# 1671079
