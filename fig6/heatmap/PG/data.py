import numpy as np
import csv
import os

def compute_angular_velocity(start_angle, start_time, end_time, final_angle):
    """
    根據提供的數據計算角速度，考慮 0° 和 360° 的循環問題。
    :param start_angle: 初始角度
    :param start_time: 開始旋轉的時間
    :param end_time: 到達最終角度的時間
    :param final_angle: 最終角度
    :return: 角速度 (°/s)
    """
    delta_angle = final_angle - start_angle
    
    # 處理缺失的 end_time
    if end_time is None:
        delta_time = (32000 - start_time) / 10000  # 替代計算時間
    else:
        delta_time = (end_time - start_time) / 10000  # 轉換時間單位
    
    # 處理 0° 和 360° 的循環問題
    if delta_angle > 180:
        delta_angle -= 360
    elif delta_angle < -180:
        delta_angle += 360
    
    return delta_angle / delta_time if delta_time != 0 else 0

# 處理多個文件並輸出 CSV
def process_files(file_list, output_csv):
    results = []
    
    for filename in file_list:
        angular_velocities = []
        with open(filename, 'r') as file:
            for line in file:
                data = list(map(lambda x: float(x) if x.strip().lower() != "none" else None, line.strip().split(',')))
                if len(data) >= 5:
                    start_angle = data[0]
                    start_time = data[1]
                    end_time = data[2]
                    final_angle = data[4]
                    
                    omega = compute_angular_velocity(start_angle, start_time, end_time, final_angle)
                    angular_velocities.append(omega)
        
        if angular_velocities:
            avg_omega = sum(angular_velocities) / len(angular_velocities)
        else:
            avg_omega = None
        
        file_name = os.path.splitext(os.path.basename(filename))[0]  # 去掉 .txt
        results.append([file_name, avg_omega])
    
    # 寫入 CSV
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Filename", "Average Angular Velocity (°/s)"])
        writer.writerows(results)
    
    print(f"結果已輸出至 {output_csv}")

# 測試處理多個文件
process_files(["LAL010.txt","LAL014.txt","LAL018.txt","LAL040.txt","LAL046.txt","LAL121.txt","LAL073.txt","LAL122.txt","LAL126.txt","LAL017.txt","LAL153.txt", "Fullmodel.txt"], "PG.csv")
