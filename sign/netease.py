#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

API_URL = "https://music.163.com"

def sign(config):
    cookie = config.get('cookie', '')
    if not cookie:
        return "未配置Cookie"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Cookie": cookie,
        "Referer": "https://music.163.com"
    }
    
    results = []
    
    # 获取用户信息（验证Cookie）
    try:
        url = f"{API_URL}/api/nuser/account/get"
        r = requests.post(url, headers=headers)
        data = r.json()
        if data.get('code') == 200:
            nickname = data.get('profile', {}).get('nickname', '未知用户')
            results.append(f"登录成功: {nickname}")
        else:
            results.append(f"Cookie验证失败: {data.get('message', '未知错误')}")
            return " | ".join(results)
    except Exception as e:
        results.append(f"验证失败: {e}")
        return " | ".join(results)
    
    # 每日签到
    try:
        url = f"{API_URL}/weapi/point/dailySignin"
        data = {"type": 0}
        r = requests.post(url, headers=headers, data=data)
        data = r.json()
        if data.get('code') == 200:
            results.append("签到成功")
        elif data.get('code') == 301:
            results.append("已签到")
        else:
            msg = data.get('msg', data.get('message', '未知'))
            results.append(f"签到: {msg}")
    except Exception as e:
        results.append(f"签到失败: {e}")
    
    # 获取用户等级
    try:
        url = f"{API_URL}/weapi/user/level"
        r = requests.post(url, headers=headers, data={})
        data = r.json()
        if data.get('code') == 200:
            level = data.get('data', {}).get('level', 0)
            results.append(f"当前等级: L{level}")
    except:
        pass
    
    return " | ".join(results) if results else "签到完成"
