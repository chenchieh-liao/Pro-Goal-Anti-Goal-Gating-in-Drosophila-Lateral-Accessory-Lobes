import numpy as np

# 產生 100 個介於 0 到 9999 的整數
numbers = np.random.randint(10000, size=100)

# 轉成字串並用 " " 包起來
formatted = ' '.join(f'"{num}"' for num in numbers)

# 加上 ranges= 前綴
output = f'ranges=( {formatted} )'

print(output)
