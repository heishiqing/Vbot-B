"""B 站匿名 SPI 接口 — 拿 buvid3 / buvid4 / b_nut cookie.

2026-06-03 修: B 站升级了 web_im/send_msg 风控, 缺 buvid3/buvid4/b_nut 会返 412 + HTML 错误页.
SPI 是 B 站给前端用的公开接口, 任何 client 都能调, 不需登录.

返回的 buvid 是设备指纹, 模块级缓存一次即可 (不要每次请求重新拉, 否则同一 bot 每分钟变身份反而像爬虫).
"""

import time
import requests

_SPI_URL = "https://api.bilibili.com/x/frontend/finger/spi"
_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# 模块级缓存 (启动后第一次调 get() 时拉, 后续复用)
_cache: dict = {}


def get() -> dict:
    """返 {"buvid3": ..., "buvid4": ..., "b_nut": ...}, 缓存. 失败返空 dict (调用方降级)."""
    global _cache
    if _cache:
        return _cache
    try:
        r = requests.get(
            _SPI_URL,
            headers={"User-Agent": _UA, "Referer": "https://www.bilibili.com/"},
            timeout=10,
        )
        if r.status_code != 200:
            return {}
        data = r.json()
        if data.get("code") != 0:
            return {}
        d = data.get("data", {}) or {}
        _cache = {
            "buvid3": d.get("b_3", ""),
            "buvid4": d.get("b_4", ""),
            # b_nut 是 buvid 同期设的整数秒时间戳, B 站 web 端逻辑
            "b_nut": str(int(time.time())),
        }
        return _cache
    except Exception:
        return {}


def reset():
    """清缓存 (eg. 怀疑 buvid 被 B 站拉黑时, 让下次 get 重新拉)."""
    global _cache
    _cache = {}
