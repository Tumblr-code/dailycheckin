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
    
    # 每日签到
    try:
        url = "https://vip.vip.qq.com/maozi/qqlogin"
        r = requests.get(url, headers=headers, allow_redirects=False)
        
        url2 = "https://vip.vip.qq.com/maozi/act/signed"
        r2 = requests.get(url2, headers=headers)
        
        if r2.status_code == 200:
            results.append("签到成功")
        else:
            results.append(f"签到: HTTP {r2.status_code}")
    except Exception as e:
        results.append(f"签到失败: {e}")
    
    # 成长值签到
    try:
        url = "https://vip.vip.qq.com/maozi/growth/sign"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            results.append("成长值签到成功")
    except Exception as e:
        results.append(f"成长值签到: {e}")
    
    return " | ".join(results) if results else "签到完成"
