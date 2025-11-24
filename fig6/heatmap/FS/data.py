import numpy as np
import csv
import os

def process_files(file_list, output_csv):
    results = []
    
    for filename in file_list:
        start_times = []

        with open(filename, 'r') as file:
            for line in file:
                data = list(map(lambda x: float(x) if x.strip().lower() != "none" else None, line.strip().split(',')))
                if len(data) >= 2:  # 確保有 start_time
                    st = data[1]
                    if st is not None:
                        start_times.append(st)

        # 計算平均 start_time（若全部為 None，則設為 32000）
        if start_times:
            avg_start_time = sum(start_times) / len(start_times)
        else:
            avg_start_time = 10000

        avg_start_time_sec = avg_start_time / 10000  # 換成秒
        file_name = os.path.splitext(os.path.basename(filename))[0]
        results.append([file_name, avg_start_time_sec])
    
    # 寫入 CSV
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Filename", "Start time (s)"])
        writer.writerows(results)
    
    print(f"平均 start_time 已輸出至 {output_csv}")

# 測試處理多個文件
process_files(["LAL010.txt","LAL014.txt","LAL018.txt","LAL040.txt","LAL046.txt","LAL121.txt","LAL073.txt","LAL122.txt","LAL126.txt","LAL017.txt","LAL153.txt", "Fullmodel.txt"], "FS.csv")
