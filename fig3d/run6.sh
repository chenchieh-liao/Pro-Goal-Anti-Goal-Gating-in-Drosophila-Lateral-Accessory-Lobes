#!/bin/bash

# 定義範圍
ranges=("0.07")

# 建立資料夾並執行程式
for range in "${ranges[@]}"
do
    # 建立目錄
    mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/${range}
    mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/${range}
    mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/${range}
    mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/${range}
    mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc_121/0/${range}
    mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc_pfl2/0/${range}
    mkdir -p /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2_121/0/${range}

    # 迴圈執行 w0 = 1 到 50
    for w0 in $(seq 1 50)
    do
        python3 control_full.py    3 ${range} $w0 & 
        python3 control_no121.py   3 ${range} $w0 &
        python3 control_noPFL2.py  3 ${range} $w0 &
        python3 control_noexcc.py  3 ${range} $w0 &
        python3 control_noexcc_no121.py 3 ${range} $w0 &
        python3 control_noexcc_nopfl2.py 3 ${range} $w0 &
        python3 control_noPFL2_no121.py 3 ${range} $w0 &

        # 等待所有進程完成
        wait

        # 移動輸出的圖片到對應的資料夾
        mv a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_ctr/0/${range}/${w0}.png
        mv 3a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no121/0/${range}/${w0}.png
        mv 5a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2/0/${range}/${w0}.png
        mv 7a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc/0/${range}/${w0}.png
        mv 8a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc_121/0/${range}/${w0}.png
        mv 9a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noexcc_pfl2/0/${range}/${w0}.png
        mv 10a.png /home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_noPFL2_121/0/${range}/${w0}.png
    done
done
