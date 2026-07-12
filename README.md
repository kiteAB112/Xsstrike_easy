# Xsstrike_easy

一个用于学习 Web 安全扫描器工程结构的简化实验项目。项目源于对 [XSStrike](https://github.com/s0md3v/XSStrike) 源码的阅读与模仿，重点是理解参数解析、请求处理与扫描流程如何组织，而非替代成熟的安全测试工具。

## 项目定位

- 作为 Python 与 Web 安全工具开发的学习记录。
- 通过较小的代码规模理解扫描器的基本模块划分。
- 不保证检测完整性、稳定性或生产可用性。

## 环境

- Python 3.9+（当前本地环境已验证 Python 3.9）
- 依赖见 `requirements.txt`

创建本地环境并安装依赖：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

可通过以下命令查看可用参数：

```powershell
.\.venv\Scripts\python.exe xsstrike.py --help
```

## 结构

```text
core/       # 配置与基础能力
modes/      # 扫描流程模块
xsstrike.py # 命令行入口
```

## 使用边界

仅可在本地靶场、课程环境或已获得明确授权的目标上使用。请勿对不属于自己的站点、服务或数据进行测试。

## 后续计划

- 补充单元测试与可复现实验记录。
- 整理参数校验和错误处理。
- 将源码阅读中的设计取舍沉淀为学习笔记。

## 致谢

本项目用于学习和复现开源安全工具的工程思路；原始灵感来自 [XSStrike](https://github.com/s0md3v/XSStrike)。
