#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import json
import time
import notify

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    if not os.path.exists(config_path):
        print("请复制 config.json.example 为 config.json 并填入Cookie")
        sys.exit(1)
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    print("=" * 50)
    print("每日签到开始")
    print("=" * 50)
    
    config = load_config()
    results = []
    
    from sign import bilibili, netease, txvideo, wps, iqiyi
    
    print("\n[1/5] 正在签到 B站 (Bilibili)...")
    try:
        result = bilibili.sign(config.get('bilibili', {}))
        results.append(("B站", result))
        print(f"  -> {result}")
    except Exception as e:
        results.append(("B站", f"失败: {str(e)}"))
        print(f"  -> 失败: {e}")
    
    print("\n[2/5] 正在签到 网易云音乐...")
    try:
        result = netease.sign(config.get('netease', {}))
        results.append(("网易云", result))
        print(f"  -> {result}")
    except Exception as e:
        results.append(("网易云", f"失败: {str(e)}"))
        print(f"  -> 失败: {e}")
    
    print("\n[3/5] 正在签到 腾讯视频...")
    try:
        result = txvideo.sign(config.get('txvideo', {}))
        results.append(("腾讯视频", result))
        print(f"  -> {result}")
    except Exception as e:
        results.append(("腾讯视频", f"失败: {str(e)}"))
        print(f"  -> 失败: {e}")
    
    print("\n[4/5] 正在签到 WPS...")
    try:
        result = wps.sign(config.get('wps', {}))
        results.append(("WPS", result))
        print(f"  -> {result}")
    except Exception as e:
        results.append(("WPS", f"失败: {str(e)}"))
        print(f"  -> 失败: {e}")
    
    print("\n[5/5] 正在签到 爱奇艺...")
    try:
        result = iqiyi.sign(config.get('iqiyi', {}))
        results.append(("爱奇艺", result))
        print(f"  -> {result}")
    except Exception as e:
        results.append(("爱奇艺", f"失败: {str(e)}"))
        print(f"  -> 失败: {e}")
    
    print("\n" + "=" * 50)
    print("签到完成")
    print("=" * 50)
    
    success_count = sum(1 for _, r in results if "成功" in r)
    print(f"成功: {success_count}/{len(results)}")
    
    msg = "【每日签到报告】\n"
    for name, result in results:
        msg += f"• {name}: {result}\n"
    
    notify.send(config.get('notify', {}), msg)
    
    return success_count == len(results)

if __name__ == '__main__':
    main()
