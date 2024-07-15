import time
import json

# リストア単体での時間を測定する関数（仮）
def measure_restore_time():
    # 実際のリストア処理を実装する必要があります
    # ここでは仮のリストア時間を返します
    return 163  # 秒

# リストア時間の基準値を設定
restore_time = measure_restore_time()
print(f"リストア単体での時間: {restore_time}秒")

# 基準時間の計算（30％増加）
threshold_time = restore_time * 1.30
print(f"基準時間: {threshold_time}秒")

# 設定をファイルに保存
with open('restore_config.json', 'w') as config_file:
    json.dump({'restore_time': restore_time, 'threshold_time': threshold_time}, config_file)

print("基準時間を設定し、ファイルに保存しました。")
