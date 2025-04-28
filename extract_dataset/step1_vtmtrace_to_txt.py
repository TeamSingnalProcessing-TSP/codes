import os
import shutil

def convert_and_move_files(source_folder, target_folder):
    # tracefiles 폴더가 없으면 생성
    os.makedirs(target_folder, exist_ok=True)
    
    # source_folder 내 모든 파일 검색
    for filename in os.listdir(source_folder):
        if filename.endswith(".vtmbmsstats"):  # 확장자 확인
            old_path = os.path.join(source_folder, filename)
            new_filename = os.path.splitext(filename)[0] + ".txt"  # 확장자 변경
            new_path = os.path.join(target_folder, new_filename)
            
            shutil.move(old_path, new_path)  # 파일 이동 및 이름 변경
            print(f"Moved: {old_path} -> {new_path}")

# 사용 예시
source_folder = "../dec_trace"  # 원본 폴더 경로
target_folder = "../tracefiles"  # 대상 폴더 경로
convert_and_move_files(source_folder, target_folder)
