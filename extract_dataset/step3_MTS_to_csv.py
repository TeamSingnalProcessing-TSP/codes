import os
import re
import csv

input_folder = 'mts_type'
output_folder = 'label'

os.makedirs(output_folder, exist_ok=True)

# 띄어쓰기도 허용하는 정규식
pattern = re.compile(r"BlockStat: POC (\d+) @\(\s*(\d+),\s*(\d+)\) \[\s*(\d+)x\s*(\d+)\] MTS_Y=(\d+)")

for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace('.txt', '.csv'))
        
        rows = []

        with open(input_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                match = pattern.search(line)
                if match:
                    poc, x, y, w, h, mts_y = match.groups()
                    rows.append([poc, x, y, w, h, mts_y])
                else:
                    if 'BlockStat' in line:
                        print(f"⚠️ 매칭 실패: {line.strip()}")  # 매칭 실패 경고

        if rows:
            with open(output_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['POC', 'pos(x)', 'pos(y)', 'blocksize(w)', 'blocksize(h)', 'MTS_Y'])
                writer.writerows(rows)
        else:
            print(f"⚠️ {filename} 파일은 저장할 데이터가 없습니다.")

print("모든 변환 완료 ✅")
