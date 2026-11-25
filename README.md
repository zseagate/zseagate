# 👋 我是 zseagate

30 年 IT 一线（1996 年入行：软件公司售后技术支持 → 企业网管 → ERP 管理员 → 企业桌面运维 → 运营商内部支撑项目带团队）。
现在一个人做**微型技术服务**，专门帮小团队排查系统故障、搭轻量化网站、用 AI 提效。

这个主页上的每个仓库都是实际干活留下的记录：**能跑通、可复现、坑都写在文档里**。

## 🔧 正在折腾

- **Ventoy 启动盘标准化模板** —— 公众号 4000+ 阅读那篇文章的配套模板（`green-future-ventoy-usb`）
- **两台 360T7 组 802.11s Mesh** —— 无线回程 + 同 SSID 无缝漫游 + mihomo 透明代理（`360t7-mesh`）
- **2009 年 Sony VAIO 复活** —— 4GB 内存跑现代 Linux + AI 编程环境（`old-laptop-revival`）
- **中文精简 Linux Mint ISO 流水线** —— rootless 构建，22.3 / 19.3 双架构（`mint-lite`）
- **本地 AI 视频生产流水线** —— 脚本 → 分镜 → 配音 → 合成 → QC，引擎可插拔（`ai-video-lab`）
- **蝉知 CMS → Joomla 5 整站迁移工具链** —— ETL、增量追平、模板 1:1 校验（`chanzhi-to-joomla`）

## 📂 项目索引

<!-- INDEX:START -->
### 🆕 新仓库（待归类）
| 项目 | 说明 |
|---|---|
| [iptv-tvbox-highend-android](https://github.com/zseagate/iptv-tvbox-highend-android) | 高配安卓机顶盒(Android 7+/9, 如创维 E900V22C) IPTV 一键方案: TiviMate 直播(盒内本地列表+分组规则) + TVBox4.1+ 点播(MacCMS 源), 定… |

### 🖥️ 旧物改造 / 系统精简
| 项目 | 说明 |
|---|---|
| [old-laptop-revival](https://github.com/zseagate/old-laptop-revival) | 2009 VAIO 跑现代 Linux + AI 全记录 |
| [mint-lite](https://github.com/zseagate/mint-lite) | 中文精简 Mint Xfce live ISO 构建流水线 |
| [mint-usb-portable](https://github.com/zseagate/mint-usb-portable) | Linux Mint 随身 U 盘（持久化 + 中文 + 常用工具） |
| [sys_init](https://github.com/zseagate/sys_init) | Debian 系装机后一站式初始化脚本 |
| [jmgo-p2-slim](https://github.com/zseagate/jmgo-p2-slim) | 坚果 P2 投影仪精简：只禁用不卸载，全程可恢复 |
| [unt413a-tv-optimization](https://github.com/zseagate/unt413a-tv-optimization) | 运营商机顶盒 debloat + IPTV |
| [iptv-tvbox-lowend-android](https://github.com/zseagate/iptv-tvbox-lowend-android) | Android 4.4 老盒子 IPTV/TVBox 兼容方案：本地直播绕开旧 TLS + MacCMS 点播，含脚本与排障（不含节目源） |
| [fcitx5-custom-phrase](https://github.com/zseagate/fcitx5-custom-phrase) | fcitx5 自定义词组脚本（附踩坑） |
| [linux-system-health-check](https://github.com/zseagate/linux-system-health-check) | Linux 系统状态自检脚本 |

### 💾 装机与 U 盘
| 项目 | 说明 |
|---|---|
| [green-future-ventoy-usb](https://github.com/zseagate/green-future-ventoy-usb) | Ventoy 启动 U 盘模板：架构、中文菜单、校验脚本 |
| [usb-bench](https://github.com/zseagate/usb-bench) | U 盘性能实测（fio）与便携 Linux 基准 |
| [disk-cleanup](https://github.com/zseagate/disk-cleanup) | Weekly cache cleanup + optional cache offload for small /home partitions |

### 🌐 网络与路由
| 项目 | 说明 |
|---|---|
| [360t7-mesh](https://github.com/zseagate/360t7-mesh) | 两台 360T7 组 Mesh 无线回程 + mihomo TUN 透明代理 |
| [bookmark-sync-notes](https://github.com/zseagate/bookmark-sync-notes) | 浏览器书签双向增量合并脚本 |

### 🪟 Windows / WSL2 与工具
| 项目 | 说明 |
|---|---|
| [wls2-setup-guide-for-windows](https://github.com/zseagate/wls2-setup-guide-for-windows) | WSL2 一站式安装管理工具箱 |
| [wsl2-jupyter-installer](https://github.com/zseagate/wsl2-jupyter-installer) | WSL2 下一键装 Jupyter 全栈 |
| [excel-image-cleaner](https://github.com/zseagate/excel-image-cleaner) | DISPIMG 图片公式批量清理（Go，离线） |
| [SilverFox-Scanner](https://github.com/zseagate/SilverFox-Scanner) | 银狐木马跨平台排查工具 |
| [python_env_trae](https://github.com/zseagate/python_env_trae) | Trae IDE + JupyterLab Python 环境搭建 |
| [dsh-shell-0xC0000135-fix](https://github.com/zseagate/dsh-shell-0xC0000135-fix) | 0xC0000135 DLL 加载失败排障全记录 |

### 🤖 AI 与网站工程
| 项目 | 说明 |
|---|---|
| [ai-video-lab](https://github.com/zseagate/ai-video-lab) | 本地 AI 视频流水线 + 开放课程套件 |
| [chanzhi-to-joomla](https://github.com/zseagate/chanzhi-to-joomla) | 蝉知 CMS → Joomla 5 迁移工具链 |
| [free-api-gateway](https://github.com/zseagate/free-api-gateway) | Local new-api gateway aggregating Numes/OpenRouter/Groq free tiers for OpenCode |
<!-- INDEX:END -->

## 📖 完整教程在公众号

每个仓库放的是**可复现的实现**；图文并茂的完整折腾记录（踩坑、对比、截图）都在公众号 **绿启未来工坊**。

## 🔗 链接

- 🌐 网站：[www.greenzx.com](https://www.greenzx.com)
- 💬 公众号：绿启未来工坊
- ✉️ 邮箱：zseagate@qq.com

> 接了单就 120% 硬核交付：每单都交排查日志（处理清单），代码摆上台面，验收先写死，不行就说不行。
<!-- AUTO-SYNC:START -->
## 🆕 仓库列表（自动同步）

> 由 GitHub Actions 按创建时间倒序自动生成，每日更新一次；**🆕** = 30 天内新建的仓库。请勿手动编辑本段，改动会被覆盖。
> 最后更新：2026-11-25 08:02 UTC

- [iptv-tvbox-highend-android](https://github.com/zseagate/iptv-tvbox-highend-android) 🆕 — 高配安卓机顶盒(Android 7+/9, 如创维 E900V22C) IPTV 一键方案: TiviMate 直播(盒内本地列表+分组规则) + TVBox4.1+ 点播(MacCMS 源), 定… · 2026-11-24
- [iptv-tvbox-lowend-android](https://github.com/zseagate/iptv-tvbox-lowend-android) 🆕 — 低版本安卓盒子(Android 4.4/API 19) IPTV 方案: TVBox4.1+ 点播(MacCMS) + TVBox Q版本地文件直播, 系统 TLS/兼容性诊断脚本 · 2026-11-22
- [free-api-gateway](https://github.com/zseagate/free-api-gateway) 🆕 — Local new-api gateway aggregating Numes/OpenRouter/Groq free tiers for OpenCode · 2026-11-21
- [disk-cleanup](https://github.com/zseagate/disk-cleanup) 🆕 — Weekly cache cleanup + optional cache offload for small /home partitions · 2026-11-20
- [usb-bench](https://github.com/zseagate/usb-bench) 🆕 — USB drive benchmark for portable Linux boot drives: batch testing, fio-based, JSON/Markdown reports… · 2026-11-03
- [unt413a-tv-optimization](https://github.com/zseagate/unt413a-tv-optimization) 🆕 — Debloat and optimize a Unionman/九联 UNT413A (Amlogic S905L3, Android 9) IPTV box: audit, scripts, Cl… · 2026-11-02
- [mint-usb-portable](https://github.com/zseagate/mint-usb-portable) 🆕 — 把 Linux Mint 22.3 完整安装到 U 盘：分区、GRUB、中文输入法、OpenCode、Remmina、星火商店与踩坑记录 · 2026-11-02
- [bookmark-sync-notes](https://github.com/zseagate/bookmark-sync-notes) 🆕 — Edge / Firefox 书签双向增量合并：脚本 + 踩坑复盘 · 2026-11-01
- [dsh-shell-0xC0000135-fix](https://github.com/zseagate/dsh-shell-0xC0000135-fix) 🆕 — 修复 DSH 无头 shell：pwsh 与 python 退出码 0xC0000135（STATUS_DLL_NOT_FOUND）排障全记录与 PATH 修复脚本 · 2026-10-30
- [ai-video-lab](https://github.com/zseagate/ai-video-lab) 🆕 — 本地优先的 AI 视频生产实验室 + 开源课程工具包：剧本 → 分镜 → 配音配乐 → 合成 → 质检 的可复现流水线，自带管理台，支持十层提示词与跨镜头一致性锚点，引擎可插拔（本地 Wan / 云… · 2026-10-29
- [360t7-mesh](https://github.com/zseagate/360t7-mesh) 🆕 — 两台 360T7 组 802.11s Mesh 无线回程 + 同 SSID 无缝漫游的实战记录（含 frequency=5745.0 浮点坑）；进阶部分用 mihomo（Clash.Meta）TUN… · 2026-10-27
- [green-future-ventoy-usb](https://github.com/zseagate/green-future-ventoy-usb) — Ventoy 启动 U 盘制作模板：架构、中文菜单与操作说明 · 2026-10-22
- [jmgo-p2-slim](https://github.com/zseagate/jmgo-p2-slim) — 坚果 JmGO P2 (Android 4.4.4) 投影仪精简实战：只禁用不卸载、存储审计、TVBox 直播源配置，全程可恢复 · 2026-10-22
- [mint-lite](https://github.com/zseagate/mint-lite) — 中文精简 Linux Mint Xfce live ISO 构建流水线（rootless，22.3 64 位 + 19.3 32 位） · 2026-10-19
- [chanzhi-to-joomla](https://github.com/zseagate/chanzhi-to-joomla) — 蝉知 CMS (ZSITE 8.x) 到 Joomla 5 的迁移工具链：ETL、多栏目补副本、增量追平、模板 1:1 校验 · 2026-10-02
- [fcitx5-custom-phrase](https://github.com/zseagate/fcitx5-custom-phrase) — 给 fcitx5 拼音 / 五笔拼音用户词库添加自定义词组的脚本（附采坑记录） · 2026-09-29
- [linux-system-health-check](https://github.com/zseagate/linux-system-health-check) — Linux 系统状态自检脚本 · 2026-08-18
- [old-laptop-revival](https://github.com/zseagate/old-laptop-revival) — 一台 2009 年的 Sony VAIO VGN-CS36H/Q，4GB 内存，Core 2 Duo 处理器，运行现代 Linux + AI 编程工具的全记录 · 2026-08-17
- [sys_init](https://github.com/zseagate/sys_init) — sys_init.sh，专为Debian系列Linux发行版设计，提供系统安装后的一站式优化配置服务。脚本兼容32位与64位架构，支持Debian 10+、Ubuntu 20.04+、MX Linu… · 2026-05-16
- [python_env_trae](https://github.com/zseagate/python_env_trae) — python环境搭建 完整启用Trae IDE安装（Trae仅提供64位版本） 包含JupyterLab及中文语言包，支持完整数据科学功能 默认预装更多科学计算包（matplotlib、scikit… · 2026-05-01
- [SilverFox-Scanner](https://github.com/zseagate/SilverFox-Scanner) — 提供跨平台的银狐(SilverFox)木马排查工具，支持Windows、Linux、macOS三大操作系统，能够快速检测木马常见的持久化机制、异常进程、恶意文件特征等，帮助个人和企业快速识别并处置银… · 2026-04-08
- [excel-image-cleaner](https://github.com/zseagate/excel-image-cleaner) — Excel Image Cleaner | Excel图片清理工具 一键批量清理Excel中的DISPIMG图片公式、嵌入图片、绘图资源，**仅删除图片相关内容，100%保留所有正常数据、公式和格式… · 2026-03-24
- [wsl2-jupyter-installer](https://github.com/zseagate/wsl2-jupyter-installer) — WSL2下一键安装Jupyter全栈环境，预装numpy/pandas/requests/python-office · 2026-03-23
- [wls2-setup-guide-for-windows](https://github.com/zseagate/wls2-setup-guide-for-windows) — WSL2 一站式安装、配置与管理工具箱，支持 Windows 10/11 · 2026-03-23

<!-- AUTO-SYNC:END -->