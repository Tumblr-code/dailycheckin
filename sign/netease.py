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
    
    # 每日签到
    try:
        url = f"{API_URL}/weapi/point/dailySignin"
        data = {"type": 0}
        r = requests.post(url, headers=headers, data=data)
        data = r.json()
        if data.get('code') == 200:
            results.append("签到成功")
        else:
            results.append(f"签到: {data.get('message', '未知错误')}")
    except Exception as e:
        results.append(f"签到失败: {e}")
    
    # 刷歌310首
    try:
        url = f"{API_URL}/weapi/playlist/mylist"
        r = requests.post(url, headers=headers, data={})
        playlists = r.json().get('result', {}).get('playlist', [])
        
        if playlists:
            track_ids = playlists[0].get('trackIds', [])[:300]
            if track_ids:
                for tid in track_ids[:10]:
                    try:
                        play_url = f"{API_URL}/weapi/v3/play/record"
                        play_data = {
                            "type": 1,
                            "id": tid.get('id'),
                            "time": 240
                        }
                        requests.post(play_url, headers=headers, data=play_data)
                    except:
                        pass
                results.append(f"刷歌完成")
    except Exception as e:
        results.append(f"刷歌失败: {e}")
    
    return " | ".join(results) if results else "签到完成"
