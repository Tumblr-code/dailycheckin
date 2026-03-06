#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

API_URL = "https://api.bilibili.com"

def sign(config):
    cookie = config.get('cookie', '')
    if not cookie:
        return "未配置Cookie"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Cookie": cookie,
        "Referer": "https://www.bilibili.com"
    }
    
    results = []
    
    # 直播签到
    try:
        url = f"{API_URL}/live/user/sign.do"
        r = requests.get(url, headers=headers)
        data = r.json()
        if data.get('code') == 0:
            results.append("直播签到成功")
        else:
            results.append(f"直播: {data.get('message', '未知错误')}")
    except Exception as e:
        results.append(f"直播签到失败: {e}")
    
    # 漫画签到
    try:
        url = f"{API_URL}/漫画/site/v2/sign"
        r = requests.post(url, headers=headers)
        data = r.json()
        if data.get('code') == 0:
            results.append("漫画签到成功")
        else:
            results.append(f"漫画: {data.get('message', '未知错误')}")
    except Exception as e:
        results.append(f"漫画签到失败: {e}")
    
    # 每日经验任务
    try:
        url = f"{API_URL}/x/web/interface/task"
        r = requests.get(url, headers=headers)
    except:
        pass
    
    # 银瓜子换硬币
    try:
        url = f"{API_URL}/x/credit/exchange/gold"
        r = requests.post(url, headers=headers)
        data = r.json()
        if data.get('code') == 0:
            results.append("银瓜子换硬币成功")
    except:
        pass
    
    return " | ".join(results) if results else "签到完成"
