import os

def extract_splitseries_lines_from_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
                for line in infile:
                    if 'MTS_Y=' in line:
                        outfile.write(line)

# 사용 예시
input_folder = '../tracefiles'  # 입력 폴더 경로
output_folder = '../mts_type'  # 출력 폴더 경로
extract_splitseries_lines_from_folder(input_folder, output_folder)
