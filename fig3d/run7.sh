#!/bin/bash

# 定義範圍
ranges=("0.07")

# 建立資料夾並執行程式
for range in "${ranges[@]}"
do
    # 建立目錄
    mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexc/0/${range}
    mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexc_121040/0/${range}
    mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexc_121040_pfl2/0/${range}
    mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexc_pfl2/0/${range}


    # 迴圈執行 w0 = 1 到 50
    for w0 in $(seq 1 50)
    do
        python3 control_noexc.py    0 ${range} $w0 & 
        python3 control_noexc_121040.py   0 ${range} $w0 &
        python3 control_noexc_121040_pfl2.py  0 ${range} $w0 &
        python3 control_noexc_pfl2.py  0 ${range} $w0 &

        # 等待所有進程完成
        wait

        # 移動輸出的圖片到對應的資料夾
        mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexc/0/${range}/${w0}.png
        mv 2a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexc_121040/0/${range}/${w0}.png
        mv 3a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexc_121040_pfl2/0/${range}/${w0}.png
        mv 4a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexc_pfl2/0/${range}/${w0}.png

    done
done
