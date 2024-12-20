# 初期設定
- ライブラリーのエラーは適時対応する

# main.pyの更新頻度,ログの出力の変更
```bash
sudo crontab -e
```

```bash
# ログを出力
0 * * * * /home/nagisa/Desktop/myvenv/bin/python /home/nagisa/Desktop/main.py >> /home/nagisa/cronjob.log 2>&1

# ログを見出力
0 * * * * /home/nagisa/Desktop/myvenv/bin/python /home/nagisa/Desktop/main.py > /dev/null 2>&1

# 10分に1回実行(デフォ)
*/10 * * * * /home/nagisa/Desktop/myvenv/bin/python /home/nagisa/Desktop/main.py > /dev/null 2>&1
```

## Cronのスケージュール表記
```scss
* * * * * コマンド
┬ ┬ ┬ ┬ ┬
│ │ │ │ │
│ │ │ │ └───── 曜日 (0 - 7) (日曜日=0 または 7)
│ │ │ └────────── 月 (1 - 12)
│ │ └────────────── 日 (1 - 31)
│ └─────────────────── 時 (0 - 23)
└─────────────────────── 分 (0 - 59)
```