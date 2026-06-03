<div align="center">

# 🤖 Vbot-B

### B 站私信自动回复机器人 · 已修 2026 风控

[![License](https://img.shields.io/badge/license-MIT-F59E0B.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.0-0E7490.svg)](#)

</div>

---

## ✨ 跟原版 BPMB 的差异

| | 原版 BPMB v1.1.1 | Vbot-B v1.0.0 |
|---|---|---|
| 发消息 | ❌ HTTP 412 风控 | ✅ HTTP 200 + 业务凭证 |
| Cookie 头 | 3 项 | **13 项** (补 9 设备指纹) |
| 失败处理 | ❌ 死循环 | ✅ 失败也跳过, 不 spam |

## 🚀 快速开始

```bash
git clone https://github.com/heishiqing/Vbot-B.git
cd Vbot-B
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 web_panel.py
```

打开 http://127.0.0.1:5000, 默认 `admin` / `admin123` (登录后改密码).

## ❤ 支持作者

<img src="static/afdian.jpg" width="240" alt="爱发电 - heishiqing">

## 📜 License

[MIT](LICENSE) · fork from [@7Hello80/BPMB](https://github.com/7Hello80/Bilibili_PrivateMessage_Bot)
