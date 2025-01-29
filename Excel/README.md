# Excel-Table-Merger

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-green.svg)](https://www.python.org/downloads/)
[![Openpyxl 3.1.2](https://img.shields.io/badge/openpyxl-3.1.2-orange.svg)](https://openpyxl.readthedocs.io/)

一个强大的 Python 脚本，用于合并 Excel 和 CSV 文件，支持保留原始格式、自动归档和日志记录。

---

## 功能特性

- **多文件格式支持**: 合并 `.xlsx`, `.xls`, `.csv` 文件。
- **格式保留**: 保留 Excel 文件的单元格样式（字体、边框、颜色）、列宽和行高。
- **路径安全处理**: 自动缩短超长路径以兼容 Windows 系统。
- **日志系统**: 记录详细操作日志，支持文件和终端双输出。
- **文件归档**: 自动备份原始文件至 `原始文件备份` 目录，避免数据覆盖。
- **智能重命名**: 自动处理重复的工作表名称（添加 `_副本` 后缀）。

---

## 快速开始

### 环境要求
- Python 3.9+
- 依赖库:  
  ```bash
  pip install pandas==2.0.3 openpyxl==3.1.2 xlrd==2.0.1
