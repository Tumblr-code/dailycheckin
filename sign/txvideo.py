#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

API_URL = "https://v.qq.com"

def sign(config):
    cookie = config.get('cookie', '')
    if not cookie:
        return "未配置Cookie"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Cookie": cookie,
        "Referer": "https://v.qq.com/"
    }
    
    results = []
    
    # 验证Cookie - 访问主页
    try:
        url = f"{API_URL}/x/login"
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            # 从cookie中提取用户名
            if 'qq_nick=' in cookie:
                nick = cookie.split('qq_nick=')[1].split(';')[0]
                nick = requests.utils.unquote(nick)
                results.append(f"登录成功: {nick}")
            else:
                results.append("登录成功")
        else:
            results.append(f"Cookie验证失败: HTTP {r.status_code}")
    except Exception as e:
        results.append(f"验证失败: {e}")
        return " | ".join(results)
    
    # 尝试签到
    try:
        url = "https://v.qq.com/x/bu/mobile_checkin"
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            results.append("签到成功")
        elif r.status_code == 404:
            results.append("签到API已更新")
    except Exception as e:
        results.append(f"签到请求失败: {str(e)[:30]}")
    
    return " | ".join(results) if results else "签到完成"
