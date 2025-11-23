for w0 in $(seq 1 50)
do 
    for w1 in $(seq 0 5 50)
    do
        python3 uni153.py 90 0.01 $w1 &
        python3 uni153no122.py 90 0.01 $w1 &
        python3 153046.py 90 0.01 $w1  &

        wait 
    done   

done

#1262505
# python3 uni153017.py 90 0.01 30 5