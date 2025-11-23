mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0


for w0 in $(seq 1 50)
do 
    python3 control_full.py 0 0.0 $w0 &
    python3 control_no040.py 0 0.0 $w0 &
    python3 control_noPFL2.py 0 0.0 $w0 &
    python3 control2_no121.py 0 0.0 $w0 &
    python3 control2_no1014.py 0 0.0 $w0 &

    wait
    mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0/${w0}.png
    mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0/${w0}.png
    mv 3a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0/${w0}.png
    mv 4a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0/${w0}.png
    mv 5a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0/${w0}.png
    

done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0.01
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0.01
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0.01
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0.01
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0.01


for w0 in $(seq 1 50)
do 
    python3 control_full.py 0 0.01 $w0 &
    python3 control_no040.py 0 0.01 $w0 &
    python3 control_noPFL2.py 0 0.01 $w0 &
    python3 control2_no121.py 0 0.01 $w0 &
    python3 control2_no1014.py 0 0.01 $w0 &

    wait
    mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0.01/${w0}.png
    mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0.01/${w0}.png
    mv 3a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0.01/${w0}.png
    mv 4a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0.01/${w0}.png
    mv 5a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0.01/${w0}.png
    

done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0.02
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0.02
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0.02
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0.02
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0.02


for w0 in $(seq 1 50)
do 
    python3 control_full.py    0 0.02 $w0 &
    python3 control_no040.py   0 0.02 $w0 &
    python3 control_noPFL2.py  0 0.02 $w0 &
    python3 control2_no121.py  0 0.02 $w0 &
    python3 control2_no1014.py 0 0.02 $w0 &

    wait
    mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0.02/${w0}.png
    mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0.02/${w0}.png
    mv 3a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0.02/${w0}.png
    mv 4a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0.02/${w0}.png
    mv 5a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0.02/${w0}.png
    

done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0.03
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0.03
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0.03
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0.03
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0.03


for w0 in $(seq 1 50)
do 
    python3 control_full.py    0 0.03 $w0 &
    python3 control_no040.py   0 0.03 $w0 &
    python3 control_noPFL2.py  0 0.03 $w0 &
    python3 control2_no121.py  0 0.03 $w0 &
    python3 control2_no1014.py 0 0.03 $w0 &

    wait
    mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0.03/${w0}.png
    mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0.03/${w0}.png
    mv 3a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0.03/${w0}.png
    mv 4a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0.03/${w0}.png
    mv 5a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0.03/${w0}.png
    

done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0.04
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0.04
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0.04
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0.04
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0.04


for w0 in $(seq 1 50)
do 
    python3 control_full.py    0 0.04 $w0 &
    python3 control_no040.py   0 0.04 $w0 &
    python3 control_noPFL2.py  0 0.04 $w0 &
    python3 control2_no121.py  0 0.04 $w0 &
    python3 control2_no1014.py 0 0.04 $w0 &

    wait
    mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0.04/${w0}.png
    mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0.04/${w0}.png
    mv 3a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0.04/${w0}.png
    mv 4a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0.04/${w0}.png
    mv 5a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0.04/${w0}.png
    

done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0.05
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0.05
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0.05
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0.05
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0.05


for w0 in $(seq 1 50)
do 
    python3 control_full.py    0 0.05 $w0 &
    python3 control_no040.py   0 0.05 $w0 &
    python3 control_noPFL2.py  0 0.05 $w0 &
    python3 control2_no121.py  0 0.05 $w0 &
    python3 control2_no1014.py 0 0.05 $w0 &

    wait
    mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0.05/${w0}.png
    mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0.05/${w0}.png
    mv 3a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0.05/${w0}.png
    mv 4a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0.05/${w0}.png
    mv 5a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0.05/${w0}.png
    

done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0.06
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0.06
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0.06
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0.06
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0.06


for w0 in $(seq 1 50)
do 
    python3 control_full.py    0 0.06 $w0 &
    python3 control_no040.py   0 0.06 $w0 &
    python3 control_noPFL2.py  0 0.06 $w0 &
    python3 control2_no121.py  0 0.06 $w0 &
    python3 control2_no1014.py 0 0.06 $w0 &

    wait
    mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0.06/${w0}.png
    mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0.06/${w0}.png
    mv 3a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0.06/${w0}.png
    mv 4a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0.06/${w0}.png
    mv 5a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0.06/${w0}.png
    

done

mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0.07
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0.07
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0.07
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0.07
mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0.07


for w0 in $(seq 1 50)
do 
    python3 control_full.py    0 0.07 $w0 &
    python3 control_no040.py   0 0.07 $w0 &
    python3 control_noPFL2.py  0 0.07 $w0 &
    python3 control2_no121.py  0 0.07 $w0 &
    python3 control2_no1014.py 0 0.07 $w0 &

    wait
    mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/0.07/${w0}.png
    mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no040/0/0.07/${w0}.png
    mv 3a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/0.07/${w0}.png
    mv 4a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/0/0.07/${w0}.png
    mv 5a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/0.07/${w0}.png
    

done

# 2873291