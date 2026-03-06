# 每日签到脚本

基于 Python 的多平台每日签到脚本，支持 GitHub Actions 自动化运行。

## 支持的平台

| 平台 | 功能 |
|------|------|
| 网易云音乐 | 每日签到、刷歌310首 |
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

复制配置文件并填入你的 Cookie：

```bash
cp config.json.example config.json
```

编辑 `config.json`，填入各平台的 Cookie：

```json
{
  "notify": {
    "type": "telegram",
    "token": "你的Telegram Bot Token",
    "user_id": "你的Telegram User ID"
  },
  "bilibili": {
    "cookie": "你的B站Cookie"
  },
  "netease": {
    "cookie": "你的网易云Cookie"
  },
  "txvideo": {
    "cookie": "你的腾讯视频Cookie"
  },
  "wps": {
    "cookie": "你的WPS Cookie"
  },
  "iqiyi": {
    "cookie": "你的爱奇艺Cookie"
  }
}
```

### 3. 运行签到

```bash
python run.py
```

## GitHub Actions 部署

### 1. Fork 本项目

### 2. 添加 Secrets

在 GitHub 仓库设置中添加以下 Secrets：

| Secret 名称 | 说明 |
|-------------|------|
| BILIBILI_COOKIE | B站 Cookie |
| NETEASE_COOKIE | 网易云音乐 Cookie |
| TXVIDEO_COOKIE | 腾讯视频 Cookie |
| WPS_COOKIE | WPS Cookie |
| IQIYI_COOKIE | 爱奇艺 Cookie |
| TELEGRAM_BOT_TOKEN | Telegram Bot Token (可选) |
| TELEGRAM_USER_ID | Telegram User ID (可选) |

### 3. 手动触发

在 Actions 页面点击 "Run workflow" 手动触发签到。

### 4. 自动运行

默认每天 20:00 (UTC+8) 自动运行。

## Cookie 获取方法

1. 登录目标网站
2. 按 F12 打开开发者工具
3. 切换到 Network（网络）标签
4. 刷新页面，点击任意请求
5. 在 Headers 中找到 Cookie，复制其值

## License

MIT License
