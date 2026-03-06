#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

API_URL = "https://vip.wps.cn"

def sign(config):
    cookie = config.get('cookie', '')
    if not cookie:
        return "未配置Cookie"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Cookie": cookie,
        "Referer": "https://vip.wps.cn/"
    }
    
    results = []
    
    # 每日签到
    try:
        url = f"{API_URL}/sign/api/signin"
        r = requests.get(url, headers=headers)
        data = r.json()
        
        if data.get('ok') or data.get('code') == 0:
            results.append("签到成功")
            if data.get('data', {}).get('reward'):
                reward = data['data']['reward']
                results.append(f"获得 {reward} 积分")
        else:
            msg = data.get('msg', data.get('message', '未知错误'))
            results.append(f"签到: {msg}")
    except Exception as e:
        results.append(f"签到失败: {e}")
    
    # 每日任务
    try:
        url = f"{API_URL}/sign/api/daily"
        r = requests.get(url, headers=headers)
        data = r.json()
        if data.get('ok') or data.get('code') == 0:
            results.append("日常任务完成")
    except:
        pass
    
    return " | ".join(results) if results else "签到完成"
