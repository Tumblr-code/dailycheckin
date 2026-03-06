# 🎯 每日签到脚本

基于 Python 的多平台每日签到脚本，支持服务器部署和 GitHub Actions 自动化运行。

## ✨ 功能特性

- 🤖 **Telegram Bot 管理** - 通过 Bot 命令手动签到、查看状态
- 📊 **签到日志** - 自动记录每次签到结果
- 🔔 **多渠道通知** - 支持 Telegram、Server酱、QMsg 推送
- ⏰ **自动签到** - 每天定时执行，无需人工干预

## 📋 支持的平台

| 平台 | 签到功能 | 状态 |
|------|----------|------|
| 🎵 网易云音乐 | 每日签到 + 刷歌310首 | ✅ |
| 📺 Bilibili | 直播签到、漫画签到、银瓜子换硬币 | ✅ |
| 🎬 腾讯视频 | 每日签到、成长值 | ✅ |
| 📝 WPS | 每日签到、日常任务 | ✅ |
| 🎥 爱奇艺 | 每日签到、日常任务 | ✅ |

---

## 🚀 快速开始

### 方式一：服务器部署（推荐）

#### 1. 克隆项目

```bash
cd /root
git clone https://github.com/Tumblr-code/dailycheckin.git
cd dailycheckin
```

#### 2. 安装依赖

```bash
python3 -m venv venv
source venv/bin/activate
pip install python-telegram-bot requests
```

#### 3. 配置 Cookie

```bash
cp config.json.example config.json
nano config.json
```

填入你的 Cookie（见下方获取教程）:

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

#### 4. 启动 Bot

```bash
# 方式一：前台运行
BOT_TOKEN="你的BotToken" python bot.py

# 方式二：后台运行（systemd）
cp dailycheckin-bot.service ~/.config/systemd/user/
nano ~/.config/systemd/user/dailycheckin-bot.service  # 修改 BOT_TOKEN
systemctl --user daemon-reload
systemctl --user enable --now dailycheckin-bot
```

---

### 方式二：GitHub Actions

#### 1. Fork 本项目

点击上方 GitHub 仓库地址，点击 **Fork**

#### 2. 添加 Secrets

进入仓库 → Settings → Secrets and variables → Actions → New repository secret

添加以下 Secrets：

| Secret 名称 | 说明 | 必需 |
|-------------|------|------|
| `BILIBILI_COOKIE` | B站 Cookie | ✅ |
| `NETEASE_COOKIE` | 网易云音乐 Cookie | ✅ |
| `TXVIDEO_COOKIE` | 腾讯视频 Cookie | ✅ |
| `WPS_COOKIE` | WPS Cookie | ✅ |
| `IQIYI_COOKIE` | 爱奇艺 Cookie | ✅ |
| `TELEGRAM_BOT_TOKEN` | Telegram Bot Token | 可选 |
| `TELEGRAM_USER_ID` | Telegram User ID | 可选 |

#### 3. 运行

- **手动触发**: 进入 Actions → Daily Sign → Run workflow
- **自动运行**: 每天 20:00 (UTC+8) 自动执行

---

## 📱 Telegram Bot 命令

| 命令 | 说明 |
|------|------|
| `/start` | 欢迎信息 |
| `/sign` | 手动触发签到 |
| `/status` | 查看今日签到状态 |
| `/log` | 查看签到日志 |
| `/help` | 帮助信息 |

---

## 🍪 Cookie 获取教程

### 通用方法（适用于所有平台）

1. **登录网站** - 用浏览器登录目标网站
2. **打开开发者工具** - 按 `F12` 或 `Ctrl+Shift+I` (Mac: `Cmd+Opt+I`)
3. **切换到 Network（网络）标签**
4. **刷新页面** - 按 `F5` 刷新
5. **点击任意请求** - 在左侧列表点击任意一个请求
6. **找到 Cookie** - 在右侧 Headers → Request Headers → 复制 Cookie 值

![Cookie获取示意](https://via.placeholder.com/800x400?text=Cookie+Getting+Guide)

---

### 各平台详细教程

#### 📺 Bilibili (B站)

1. 登录 [B站](https://www.bilibili.com)
2. 打开开发者工具 (F12)
3. 刷新页面
4. 点击 `www.bilibili.com` 请求
5. 复制 Request Headers 中的 Cookie
6. **注意**：需要包含 `SESSDATA` 字段

#### 🎵 网易云音乐

1. 登录 [网易云音乐](https://music.163.com)
2. 打开开发者工具
3. 点击任意请求
4. 复制 Cookie（注意：需要包含 `__csrf` 字段）

#### 🎬 腾讯视频

1. 登录 [腾讯视频](https://v.qq.com)
2. 打开开发者工具
3. 刷新页面
4. 复制 Cookie（建议包含 `qq_id` 相关字段）

#### 📝 WPS

1. 登录 [WPS](https://vip.wps.cn)
2. 打开开发者工具
3. 刷新页面
4. 复制 Cookie

#### 🎥 爱奇艺

1. 登录 [爱奇艺](https://www.iqiyi.com)
2. 打开开发者工具
3. 刷新页面
4. 复制 Cookie

---

### 🔒 安全提示

- ✅ Cookie 仅用于签到，不会泄露给第三方
- ✅ 建议定期更新 Cookie（某些平台 Cookie 有效期较短）
- ✅ 不要将 Cookie 提交到 GitHub 公开仓库
- ✅ 本地部署时确保 `config.json` 权限正确：`chmod 600 config.json`

---

## 📝 管理命令

### 服务器部署

```bash
# 查看 Bot 状态
systemctl --user status dailycheckin-bot

# 重启 Bot
systemctl --user restart dailycheckin-bot

# 停止 Bot
systemctl --user stop dailycheckin-bot

# 查看日志
journalctl --user -u dailycheckin-bot -f
```

### 手动运行签到

```bash
# 激活虚拟环境
source venv/bin/activate

# 运行签到
python run.py
```

---

## 🔧 常见问题

### Q: 签到失败怎么办？

A: 
1. 检查 Cookie 是否过期，重新获取
2. 查看日志确认具体错误信息
3. 部分平台需要验证码或账号异常

### Q: 如何查看签到日志？

A: 
- Telegram Bot 中使用 `/log` 命令
- 服务器上查看 `sign.log` 文件

### Q: Bot 无法启动？

A: 
1. 确认 BOT_TOKEN 正确
2. 检查 Python 依赖是否安装完整
3. 查看日志：`journalctl --user -u dailycheckin-bot`

---

## 📄 License

MIT License

---

## 🤝 感谢

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Telegram Bot 框架
- [cafebox/dailysign](https://github.com/cafebox/dailysign) - 签到脚本参考
