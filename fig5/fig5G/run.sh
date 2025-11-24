for w0 in $(seq 1 30)
do 
    for w1 in $(seq 0 5 50)
    do
        python3 AG_cl_full_model.py 0.01 90 20 9 4 $w1 &
        python3 AG_cl_full_model.py 0.01 45 20 9 4 $w1 &
        python3 AG_cl_full_model.py 0.01 135 20 9 4 $w1 &
        python3 AG_cl_full_model.py 0.01 30 20 9 4 $w1 &
        python3 AG_cl_full_model.py 0.01 60 20 9 4 $w1 &
        python3 AG_cl_full_model.py 0.01 120 20 9 4 $w1 &
        python3 AG_cl_full_model.py 0.01 150 20 9 4 $w1 &

        wait 
    done   

done