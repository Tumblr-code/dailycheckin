# 每日签到脚本

基于 Python 的多平台每日签到脚本，支持 GitHub Actions 自动化运行。

## 支持的平台

| 平台 | 功能 |
|------|------|
| 网易云音乐 | 每日签到、刷歌 |
| Bilibili | 直播签到、漫画签到、银瓜子换硬币 |
| 腾讯视频 | 每日签到、成长值 |
| WPS | 每日签到、日常任务 |
| 爱奇艺 | 每日签到、日常任务 |

## 本地运行

### 1. 安装依赖

```bash
pip install requests
```

### 2. 配置 Cookie

```bash
cp config.json.example config.json
```

### 3. 运行签到

```bash
python run.py
```

## GitHub Actions

默认每天 20:00 (UTC+8) 自动运行。
