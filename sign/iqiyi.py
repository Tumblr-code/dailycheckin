#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import time

API_URL = "https://tc.iqiyi.com"

def sign(config):
    cookie = config.get('cookie', '')
    if not cookie:
        return "未配置Cookie"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Cookie": cookie,
        "Referer": "https://www.iqiyi.com/"
    }
    
    results = []
    
    # 每日签到
    try:
        url = f"{API_URL}/tc/quick/qp_sign"
        r = requests.get(url, headers=headers)
        data = r.json()
        
        if data.get('code') == 0 or data.get('success'):
            results.append("签到成功")
            if data.get('data', {}).get('rewardName'):
                results.append(f"获得 {data['data']['rewardName']}")
        else:
            msg = data.get('msg', data.get('message', '未知错误'))
            results.append(f"签到: {msg}")
    except Exception as e:
        results.append(f"签到失败: {e}")
    
    # 每日任务
    try:
        url = f"{API_URL}/tc/quick/task/get"
        r = requests.get(url, headers=headers)
        data = r.json()
        if data.get('code') == 0:
            tasks = data.get('data', {}).get('taskList', [])
            for task in tasks:
                if task.get('taskStatus') == 0:
                    task_id = task.get('taskId')
                    task_url = f"{API_URL}/tc/quick/task/finish/{task_id}"
                    try:
                        requests.get(task_url, headers=headers)
                    except:
                        pass
            results.append("日常任务完成")
    except:
        pass
    
    return " | ".join(results) if results else "签到完成"
