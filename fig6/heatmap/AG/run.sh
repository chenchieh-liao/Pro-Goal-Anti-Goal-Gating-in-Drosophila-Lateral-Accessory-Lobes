for w0 in $(seq 1 30)
do
    nohup python3 FPL_0701cl0.py  0.01 90 20 9 4 250 50 50 &
    nohup python3 FPL_0701cl1.py  0.01 90 20 9 4 250 50 50 &
    nohup python3 FPL_0701cl2.py  0.01 90 20 9 4 250 50 50 &
    nohup python3 FPL_0701cl3.py  0.01 90 20 9 4 250 50 100 &
    nohup python3 FPL_0701cl4.py  0.01 90 20 9 4 250 50 50 &
    nohup python3 FPL_0701cl5.py  0.01 90 20 9 4 250 50 150 &
    nohup python3 FPL_0701cl6.py  0.01 90 20 9 4 250 50 50 &
    nohup python3 FPL_0701cl7.py  0.01 90 20 9 4 250 50 50 &
    nohup python3 FPL_0701cl8.py  0.01 90 20 9 4 250 50 50 &
    nohup python3 FPL_0701cl9.py  0.01 90 20 9 4 250 50 50 &
    nohup python3 FPL_0701cl10.py 0.01 90 20 9 4 250 50 50 &
    nohup python3 FPL_0701cl11.py 0.01 90 20 9 4 250 50 150 &
    wait
done