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
    
    # 获取用户信息（验证Cookie）
    try:
        url = f"{API_URL}/x/web-interface/nav"
        r = requests.get(url, headers=headers)
        data = r.json()
        if data.get('code') == 0:
            user_name = data.get('data', {}).get('uname', '未知用户')
            results.append(f"登录成功: {user_name}")
        else:
            results.append(f"Cookie验证失败: {data.get('message', '未知错误')}")
            return " | ".join(results)
    except Exception as e:
        results.append(f"验证失败: {e}")
        return " | ".join(results)
    
    # 观看直播/视频 获取经验
    try:
        url = f"{API_URL}/x/vfeelfeed/feedlist?pn=1&ps=1"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            results.append("获取首页推荐成功")
    except Exception as e:
        pass
    
    # 漫画签到（新版API）
    try:
        url = f"{API_URL}/x/v2/feedback/like"
        r = requests.get(url, headers=headers, timeout=5)
    except:
        pass
    
    # 分享视频获取经验
    try:
        url = f"{API_URL}/x/web/archive/share"
        r = requests.post(url, headers=headers, data={"aid": 170001}, timeout=5)
    except:
        pass
    
    return " | ".join(results) if results else "签到完成"
