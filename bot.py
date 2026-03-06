#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import json
import datetime
import subprocess
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN', '')

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    if not os.path.exists(config_path):
        return None
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_log(message):
    log_file = os.path.join(os.path.dirname(__file__), 'sign.log')
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 每日签到 Bot\n\n"
        "可用命令：\n"
        "/start - 欢迎信息\n"
        "/sign - 立即签到\n"
        "/status - 查看今日状态\n"
        "/log - 查看签到日志\n"
        "/help - 帮助信息"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 帮助\n\n"
        "/sign - 手动触发签到\n"
        "/status - 查看今日签到状态\n"
        "/log - 查看最近签到日志\n"
        "\n每天自动签到时间: 20:00"
    )

async def sign_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔄 正在执行签到，请稍候...")
    
    try:
        result = subprocess.run(
            ['python3', 'run.py'],
            capture_output=True,
            text=True,
            timeout=300
        )
        output = result.stdout + result.stderr
        
        save_log(f"手动签到: {output[:500]}")
        
        await update.message.reply_text(
            f"✅ 签到完成！\n\n{output[:3000]}"
        )
    except Exception as e:
        await update.message.reply_text(f"❌ 签到失败: {str(e)}")

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_file = os.path.join(os.path.dirname(__file__), 'sign.log')
    
    if not os.path.exists(log_file):
        await update.message.reply_text("📊 暂无签到记录")
        return
    
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        today_logs = [l for l in lines if today in l]
        
        if not today_logs:
            await update.message.reply_text(f"📊 今日 ({today}) 暂无签到记录")
        else:
            await update.message.reply_text(
                f"📊 今日签到状态 ({today})\n\n" + "".join(today_logs[-10:])
            )
    except Exception as e:
        await update.message.reply_text(f"❌ 读取失败: {str(e)}")

async def log_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_file = os.path.join(os.path.dirname(__file__), 'sign.log')
    
    if not os.path.exists(log_file):
        await update.message.reply_text("📝 暂无日志")
        return
    
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        recent = lines[-20:] if len(lines) > 20 else lines
        
        await update.message.reply_text(
            "📝 最近签到日志\n\n" + "".join(recent)
        )
    except Exception as e:
        await update.message.reply_text(f"❌ 读取失败: {str(e)}")

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❓ 未知命令，输入 /help 查看可用命令"
    )

def main():
    if not BOT_TOKEN:
        print("请设置环境变量 BOT_TOKEN")
        sys.exit(1)
    
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("sign", sign_command))
    application.add_handler(CommandHandler("status", status_command))
    application.add_handler(CommandHandler("log", log_command))
    application.add_handler(MessageHandler(filters.COMMAND, unknown_command))
    
    print("🤖 Bot 已启动...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
