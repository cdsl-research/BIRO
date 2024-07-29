# Backup-Interrupting Restore Optimization

このプロジェクトは，バックアップ中のリストアにおけるリストア時間の増加を最小限に抑えるための提案手法を実装したものです．特に，バックアップ中にリストアを行った際のリストア時間が単体で行った時間の38%増加する場合に，バックアップに使用されるCPU使用量を制限し，リストアを優先させる方法を提案します．

## 構成

- `monitor.py` : バックアップを行っていない時にリストア単体で行った時間を測定し，基準値を設定する．また，バックアップ中にリストアが行われた際の状況を一定間隔で進行状況を監視する．
- `res_manager.py` : バックアップにおけるCPU使用量の制限を行い，リストアが完了したら制限を解除する．

## 使用方法

### 前提条件

- Python3がインストールされていること

### 実行手順

1. リストア単体の時間を測定し，基準値を設定します．
    ```bash
    python3 monitor.py
    ```

2. バックアップ中にリストアが行われた際の状況を監視します．進行状況を一定間隔で取得し，予測完了時間を計算します．CPU使用量の制限が必要な場合には `res_manager.py` が自動的に呼び出されます．
    ```bash
    python3 monitor.py
    ```

3. CPU使用量の制限を行います．
    ```bash
    python3 res_manager.py limit
    ```

4. CPU使用量の制限を解除します．
    ```bash
    python3 res_manager.py reset
    ```

## 実行結果の例

### `monitor.py` の実行結果

リストア単体の時間が163秒と測定され，基準値（リストア時間）は163秒，許容時間（基準値の38%増加）は163 * 1.38 ≈ 225秒と設定されます．

バックアップ中にリストアが開始され，リストアが開始されてから50秒経過した時点でリストア進行状況が20%完了し，予測完了時間は250秒となりました．許容時間を超えるため，CPU使用量の制限が行われました．

```bash
リストア進行状況を監視中...
経過時間: 10秒, 進行状況: 5%
経過時間: 20秒, 進行状況: 10%
経過時間: 30秒, 進行状況: 15%
経過時間: 40秒, 進行状況: 18%
経過時間: 50秒, 進行状況: 20%
予測完了時間: 250秒
リストア時間が許容時間を超えるため，CPU使用量を制限します．
```

### `res_manager.py` の実行結果
CPU使用量の制限を行い，その後制限を解除する手順の結果です．

### CPU使用量の制限：
```bash
$ python3 res_manager.py limit
CPU使用量を制限しました．
```

### CPU使用量の制限を解除：
```bash
$ python3 res_manager.py reset
CPU使用量の制限を解除しました．
```
