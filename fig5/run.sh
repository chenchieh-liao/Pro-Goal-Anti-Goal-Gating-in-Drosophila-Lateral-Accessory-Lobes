for w0 in $(seq 1 10)
do 

    python3 PFL3+PFL2.py 0.01 90 20 9 4 0 &
    python3 PFL3+PFL2.py 0.01 45 20 9 4 0 &
    python3 PFL3+PFL2.py 0.01 135 20 9 4 0 &
    python3 PFL3+PFL2.py 0.01 30 20 9 4 0 &
    python3 PFL3+PFL2.py 0.01 60 20 9 4 0 &
    python3 PFL3+PFL2.py 0.01 120 20 9 4 0 &
    python3 PFL3+PFL2.py 0.01 150 20 9 4 0 &

    wait 
     

done