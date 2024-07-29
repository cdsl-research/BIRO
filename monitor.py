import time
import csv
import os
from datetime import datetime
from subprocess import call, check_output

# 基準値と許容時間を設定する関数
def set_thresholds(restore_time, increase_percentage=0.38):
    threshold_time = restore_time * (1 + increase_percentage)
    return threshold_time

# リストア時間を測定する関数
def measure_restore_time():
    # 実際のリストア処理を行い、リストア時間を計測する
    # 仮のリストア処理としてスリープを使用（実際のリストア処理をここに実装）
    start_time = time.time()
    time.sleep(163)  # 仮のリストア時間
    restore_time = time.time() - start_time
    return restore_time

# リアルタイムでリストアの進行状況を監視する関数
def monitor_restore(threshold_time, interval=10):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        # ここで実際の進行状況（パーセンテージ）を取得する
        # 仮に進行状況を設定（実際の進行状況取得ロジックをここに実装）
        progress_percentage = get_restore_progress()  # 実際の進行状況取得関数

        if progress_percentage >= 100:
            break

        predicted_time = elapsed_time / (progress_percentage / 100)
        if predicted_time > threshold_time:
            return False  # 許容時間を超える予測

        time.sleep(interval)
    
    return True  # 許容時間内に完了

# リストア進行状況を取得する仮の関数（実際の取得ロジックを実装）
def get_restore_progress():
    # 実際にはリストア進行状況を取得するロジックを実装する
    return 50  # 仮の進行状況

# 結果をCSVファイルに保存する関数
def save_result_to_csv(vm_name, restore_time, threshold_time):
    filename = 'restore_times.csv'
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["VM_Name", "Restore_Time", "Threshold_Time", "Timestamp"])
        writer.writerow([vm_name, restore_time, threshold_time, datetime.now()])

def main():
    restore_time = measure_restore_time()
    threshold_time = set_thresholds(restore_time)
    
    save_result_to_csv("VM_Name", restore_time, threshold_time)

    if not monitor_restore(threshold_time):
        # CPU使用量の制限を行う
        call(["python3", "res_manager.py", "limit"])
    else:
        # CPU使用量の制限を解除する
        call(["python3", "res_manager.py", "reset"])

if __name__ == "__main__":
    main()
