#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

def send(config, message):
    if not config:
        print("  [通知] 未配置通知，跳过")
        return
    
    notify_type = config.get('type', '').lower()
    
    if notify_type == 'telegram':
        token = config.get('token', '')
        user_id = config.get('user_id', '')
        if token and user_id:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            data = {"chat_id": user_id, "text": message}
            try:
                requests.post(url, data=data)
                print("  [通知] Telegram 发送成功")
            except Exception as e:
                print(f"  [通知] Telegram 发送失败: {e}")
        else:
            print("  [通知] Telegram 配置不完整")
    
    elif notify_type == 'qmsg':
        qmsg_key = config.get('qmsg_key', '')
        if qmsg_key:
            url = f"https://qmsg.zendee.cn/send/{qmsg_key}"
            data = {"msg": message}
            try:
                requests.post(url, data=data)
                print("  [通知] QMsg 发送成功")
            except Exception as e:
                print(f"  [通知] QMsg 发送失败: {e}")
    
    elif notify_type == 'serverchan':
        sckey = config.get('sckey', '')
        if sckey:
            url = f"https://sc.ftqq.com/{sckey}.send"
            data = {"text": "每日签到", "desp": message}
            try:
                requests.post(url, data=data)
                print("  [通知] Server酱 发送成功")
            except Exception as e:
                print(f"  [通知] Server酱 发送失败: {e}")
    
    else:
        print(f"  [通知] 未知的通知类型: {notify_type}")
