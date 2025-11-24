import csv

def compute_diff_normalized_by_max_diff(input_csv, output_csv):
    data = {}

    # 讀取 CSV 檔案
    with open(input_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            filename = row["Filename"]
            try:
                avg_velocity = float(row["Start time (s)"])
            except ValueError:
                avg_velocity = None
            data[filename] = avg_velocity

    # 取得 Fullmodel 的角速度
    fullmodel_velocity = data.get("Fullmodel", None)
    if fullmodel_velocity is None:
        print("缺少 Fullmodel 的資料。")
        return

    # 計算差值
    raw_diffs = []
    for filename, velocity in data.items():
        if filename != "Fullmodel" and velocity is not None:
            diff = fullmodel_velocity - velocity 
            raw_diffs.append((filename, diff))

    if not raw_diffs:
        print("沒有其他有效資料可比對。")
        return

    # 找出最大絕對差值
    max_abs_diff = max(abs(diff) for _, diff in raw_diffs)
    if max_abs_diff == 0:
        print("所有模型與 Fullmodel 差值為 0，無法標準化。")
        return

    # 標準化差值
    normalized_diffs = [
        [filename, diff / max_abs_diff] for filename, diff in raw_diffs
    ]

    # 寫入結果
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Filename", "Normalized Difference (by max |diff|)"])
        writer.writerows(normalized_diffs)

    print(f"差值已輸出至 {output_csv}")

# 執行
compute_diff_normalized_by_max_diff("RS.csv", "RS_diff.csv")
