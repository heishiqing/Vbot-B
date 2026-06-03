<div align="center">

# 🤖 Vbot-B

### B 站私信自动回复机器人

[![License](https://img.shields.io/badge/license-MIT-F59E0B.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.0-0E7490.svg)](#)

</div>

---

## ✨ 功能特性

**消息回复**
- 🔑 **关键词自动回复** — 全局 + 账号专属双层字典, `;` 分隔多关键词触发同一回复, contains / exact 两种匹配模式
- 🖼️ **图片回复** — `[bili_image:xxx]` 占位符直接发图, 支持 JPG/PNG/GIF/WebP
- 👤 **@对方昵称** — `[at_user]` 占位符自动替换粉丝昵称, 加亲切感
- 🔌 **插件系统** — `plugins/` 目录扔 .py 模块即可扩展, 字典 miss 时插件优先接管

**账号 & 粉丝管理**
- 🎫 **多账号并行** — 一个 web 面板管 N 个 B 站号, 每号独立线程 + 关键词配置
- 📱 **二维码登录** — 面板内直接扫码, 自动写回 cookie, 无需手动复制 SESSDATA
- 💫 **新粉欢迎** — 自动检测新关注 → 私信欢迎语 + 可选自动回关
- 🩺 **健康监控** — 每账号实时显示 cookie 有效性, 掉线红色告警

**面板运维**
- 📊 **实时流水** — 看每条私信 `replied / unmatched / reply_failed` 状态 + 来源 talker_id
- 🪵 **运行日志** — 浏览器内实时查看 bot stdout, 不用 SSH 看 log
- ⚙️ **图床管理** — 上传图片到面板, 自动生成 `[bili_image:xxx]` 引用串
- 🔐 **admin 鉴权** — Flask session + 密码 hash, 多设备同登录

## 🛠 Vbot-B 比原版 BPMB v1.1.1 修了什么

| | 原版 | Vbot-B |
|---|---|---|
| 发消息 | ❌ HTTP 412 风控 + HTML 错误页 | ✅ HTTP 200 + code 0 业务凭证 |
| Cookie 头 | 3 项 | **13 项** (补 9 设备指纹: buvid3/4/b_nut/buvid_fp/ckMd5/_uuid 等) |
| 失败处理 | ❌ 死循环 (失败不标记, 5s 重试同一条触发更深风控) | ✅ 失败也标记跳过 |
| 可观测 | ❌ 只打 HTTP status | ✅ 完整 response body + bili-trace-id |

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

如果 Vbot-B 帮你省了时间, 欢迎请作者一杯咖啡 ☕

<img src="static/afdian.jpg" width="240" alt="爱发电 - heishiqing">

## 📜 License

[MIT](LICENSE) · fork from [@7Hello80/BPMB](https://github.com/7Hello80/Bilibili_PrivateMessage_Bot)
