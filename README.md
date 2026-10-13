**简体中文** · [English](README.en.md)

# Z.A.T.O. // 我爱这世界与世间万物 — 汉化补丁

**Z.A.T.O. // I Love the World and Everything in It** 的非官方简体中文汉化补丁。

原作：Ferry（Nopanamaman），2025 · 引擎：Ren'Py 8.0.3

- **Steam 商店页面**：<https://store.steampowered.com/app/4122860/ZATO__I_Love_the_World_and_Everything_In_It/>（App ID `4122860`，免费游戏）
- **itch.io 页面**：<https://nopanamaman.itch.io/z-a-t-o-i-love-the-world-and-everything-in-it>

## 🎮 游戏与适配版本信息

| 项目 | 信息 |
| --- | --- |
| 游戏名称 | Z.A.T.O. // I Love the World and Everything in It |
| 开发 / 发行 | Ferry // Nopanamaman |
| 适配游戏版本 | **v1.0**（Steam 当前版本，`config.version = "1.0"`） |
| 游戏引擎 | Ren'Py **8.0.3**（脚本版本 `(8, 0, 3)`） |
| 适配平台 | Windows（Steam 发行版；Mac / Linux 理论通用，未测试） |
| 汉化基准 | Steam 版 `scripts.rpa`（16 个脚本文件）全量文本 |
| 补丁版本 | v1.0 |

> [!NOTE]
> 补丁以文本方式注入 `game/tl/chinese/`，不修改任何游戏原文件与归档。游戏更新后若脚本文本未变动，补丁通常可直接继续使用；若官方后续版本内置官方中文，建议优先使用官方翻译。

## ✨ 特性

- **全文本汉化**：覆盖序章、第一章、第二章全部七天与终章（共约 12,300 句台词与界面文本），包括章节跳转、画廊、设置、操作说明、制作人员名单等全部 UI。
- **双语并存**：正文采用「中文为主、英文原文以小号灰字附后」的双语排版，可对照原文阅读，风格贴合原作。
- **开机即中文**：通过 `config.language` 强制加载中文语言包，无需任何设置。
- **界面完整适配**：替换原版 Courier 字体为[思源黑体](https://github.com/adobe-fonts/source-han-sans)（SIL OFL 开源协议，随补丁分发），并调整了字号；西里尔字母自动回退到内置 DejaVu Sans，片尾俄文正常显示。
- **保留原作风味**：文字特效（`{w}`、`{cps}`、`{size}`、{i} 斜体等）、打字机节奏、NVL 段落、彩蛋文本全部原样保留。

## 📦 安装

1. 定位游戏目录（Steam 默认）：
   ```
   C:\Program Files (x86)\Steam\steamapps\common\Z.A.T.O.  I Love the World and Everything In It\
   ```
   （也可从 Steam 库中右键游戏 → 管理 → 浏览本地文件直达。）
2. 将本补丁的 `game/` 文件夹**整体复制**进游戏目录，选择「替换目标中的文件」。完成后游戏目录中应出现：
   ```
   Z.A.T.O. ...\
   ├─ game\
   │  ├─ 00zh_override.rpy          ← 新增
   │  └─ tl\
   │     └─ chinese\                ← 新增（含字体）
   └─ ...
   ```
3. 启动游戏即可。存档与原版完全兼容。

### 卸载

删除 `game/00zh_override.rpy` 与 `game/tl/` 两个项目即可恢复原版。

## 🔤 字体说明

补丁使用 **思源黑体精简版（SourceHanSansLite.ttf）**，来自 Ren'Py 官方 SDK，以 [SIL Open Font License](https://openfontlicense.org/) 授权分发，可自由 redistribution。原版 Courier 字体不含任何中文字形，故中文界面必须替换字体。

## ⚠️ 已知事项

- 原版图片内嵌的少量英文（如标题画面 logo）不属于文本，无法汉化。
- 制作名单中「配音：Воробушек」等俄文人名为专有名词，保留原文。

## 📄 授权

- 本补丁的翻译文本仅供学习交流，禁止商用；游戏一切权利归原作者 Ferry（Nopanamaman）所有。
- `fonts/SourceHanSansLite.ttf` 依 SIL OFL 1.1 授权分发，版权 © Adobe。
- 游戏本体在 Steam 与 itch.io 均为**免费**，请前往官方页面支持作者。
