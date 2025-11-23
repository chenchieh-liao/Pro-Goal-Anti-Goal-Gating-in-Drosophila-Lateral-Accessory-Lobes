mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no073/90
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no126/90

for w0 in $(seq 1 50)
do 
    python3 control.py 90 0.01 $w0 &
    python3 control2.py 90 0.01 $w0 &
    wait
    mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no126/90/${w0}.png
    mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no073/90/${w0}.png
done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no073/60
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no126/60

for w0 in $(seq 1 50)
do 
    python3 control.py 120 0.01 $w0 &
    python3 control2.py 120 0.01 $w0 &
    wait
    mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no126/60/${w0}.png
    mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no073/60/${w0}.png
done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no073/75
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no126/75

for w0 in $(seq 1 50)
do 
    python3 control.py 105 0.01 $w0 &
    python3 control2.py 105 0.01 $w0 &
    wait
    mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no126/75/${w0}.png
    mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig2d/data_no073/75/${w0}.png
done

# 1697449

