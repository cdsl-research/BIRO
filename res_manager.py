import sys
import subprocess

# CPU使用量を制限する関数
def limit_cpu_usage():
    # 実際のCPU制限コマンドを実行する
    # 以下は仮のコマンド例（実際の環境に合わせて変更すること）
    command = ["esxcli", "hardware", "cpu", "list"]
    try:
        subprocess.run(command, check=True)
        print("CPU使用量を制限しました")
    except subprocess.CalledProcessError as e:
        print(f"CPU制限エラー: {e}")

# CPU使用量の制限を解除する関数
def reset_cpu_usage():
    # 実際のCPU制限解除コマンドを実行する
    # 以下は仮のコマンド例（実際の環境に合わせて変更すること）
    command = ["esxcli", "hardware", "cpu", "unlist"]
    try:
        subprocess.run(command, check=True)
        print("CPU使用量の制限を解除しました")
    except subprocess.CalledProcessError as e:
        print(f"CPU制限解除エラー: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 res_manager.py <limit|reset>")
        sys.exit(1)

    action = sys.argv[1]
    if action == "limit":
        limit_cpu_usage()
    elif action == "reset":
        reset_cpu_usage()
    else:
        print("Unknown action:", action)
        sys.exit(1)

if __name__ == "__main__":
    main()
