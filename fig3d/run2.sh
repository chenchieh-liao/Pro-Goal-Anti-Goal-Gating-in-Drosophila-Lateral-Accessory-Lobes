mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0



for w0 in $(seq 1 10)
do 
    python3 control_no1014c.py 0 0.0 $w0 &
    python3 control_noexcc.py 0 0.0 $w0 &


    wait
    mv 6a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0/${w0}.png
    mv 7a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0/${w0}.png

    

done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0.01
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0.01


for w0 in $(seq 1 10)
do 
    python3 control_no1014c.py 0 0.01 $w0 &
    python3 control_noexcc.py 0 0.01 $w0 &


    wait
    mv 6a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0.01/${w0}.png
    mv 7a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0.01/${w0}.png

    

done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0.02
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0.02



for w0 in $(seq 1 10)
do 
    python3 control_no1014c.py    0 0.02 $w0 &
    python3 control_noexcc.py   0 0.02 $w0 &


    wait
    mv 6a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0.02/${w0}.png
    mv 7a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0.02/${w0}.png

    

done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0.03
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0.03



for w0 in $(seq 1 10)
do 
    python3 control_no1014c.py    0 0.03 $w0 &
    python3 control_noexcc.py   0 0.03 $w0 &


    wait
    mv 6a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0.03/${w0}.png
    mv 7a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0.03/${w0}.png

    

done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0.04
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0.04



for w0 in $(seq 1 10)
do 
    python3 control_no1014c.py    0 0.04 $w0 &
    python3 control_noexcc.py   0 0.04 $w0 &


    wait
    mv 6a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0.04/${w0}.png
    mv 7a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0.04/${w0}.png
 
    

done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0.05
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0.05



for w0 in $(seq 1 10)
do 
    python3 control_no1014c.py    0 0.05 $w0 &
    python3 control_noexcc.py   0 0.05 $w0 &


    wait
    mv 6a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0.05/${w0}.png
    mv 7a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0.05/${w0}.png

    

done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0.06
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0.06



for w0 in $(seq 1 10)
do 
    python3 control_no1014c.py    0 0.06 $w0 &
    python3 control_noexcc.py   0 0.06 $w0 &


    wait
    mv 6a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0.06/${w0}.png
    mv 7a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0.06/${w0}.png


done

# mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0.07
# mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0.07



# for w0 in $(seq 1 10)
# do 
#     python3 control_no1014c.py    0 0.07 $w0 &
#     python3 control_noexcc.py   0 0.07 $w0 &


#     wait
#     mv 6a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014c/0/0.07/${w0}.png
#     mv 7a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/0.07/${w0}.png

    

# done

# 2873291