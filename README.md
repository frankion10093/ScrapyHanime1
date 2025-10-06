# Spider1 - Hanime1视频爬虫

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Scrapy](https://img.shields.io/badge/Scrapy-2.13.3-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

一个基于Scrapy框架的网络爬虫项目，用于从hanime1.me网站爬取视频内容。

## ⚠️ 重要声明

### 法律与道德声明
- **仅供学习和交流**：本项目仅用于技术学习和研究目的
- **非商业用途**：严禁用于任何商业用途或盈利目的
- **尊重版权**：不鼓励非法爬取受版权保护的内容
- **责任自负**：使用者需自行承担使用本项目可能带来的法律责任

### 使用要求
- **网络要求**：由于目标网站的访问限制，使用本爬虫需要配置科学上网（VPN/代理）
- **合规使用**：请确保您的使用行为符合当地法律法规和网站的使用条款

## 🚀 功能特性

- 支持多页爬取（1-70页）
- 自动解析视频链接
- 本地视频文件下载
- 自定义文件命名
- 支持CSS选择器解析

## 📦 安装依赖

```bash
在存在requirement.txt的目录下执行
pip install -r requirement.txt
```

或手动安装：
```bash
pip install scrapy==2.13.3 requests==2.32.5 lxml==6.0.2
```

## 🛠 使用方法

1. **配置网络**：确保已配置好科学上网工具
2. **运行爬虫**：
   ```bash
   python run.py
   ```
3. **查看结果**：下载的视频将保存在 `D:\dianying\` 目录

## 📁 项目结构

```
spider1/
├── spiders/
│   ├── hanime1.py      # 主爬虫文件
│   └── requirement.txt # 依赖文件
├── items.py           # 数据项定义
├── middlewares.py     # 中间件
├── pipelines.py       # 数据处理管道
├── settings.py        # 项目配置
└── __init__.py
```

## ⚙️ 配置说明

主要配置在 `settings.py` 中：
- `USER_AGENT`: 浏览器标识
- `ROBOTSTXT_OBEY`: 遵守robots.txt规则
- `FEED_EXPORT_ENCODING`: 输出编码为UTF-8

## 🔧 自定义配置

您可以修改以下参数：
- 在 `hanime1.py` 中修改爬取页数范围
- 在 `settings.py` 中调整并发和延迟设置
- 修改下载目录路径

## ❓ 常见问题

**Q: 爬虫无法访问网站？**
A: 请检查网络连接，确保已配置科学上网工具

**Q: 下载速度慢？**
A: 可以调整 `settings.py` 中的 `CONCURRENT_REQUESTS` 和 `DOWNLOAD_DELAY`

**Q: 如何修改保存路径？**
A: 在 `hanime1.py` 的 `download_video` 函数中修改保存路径

## 📝 开发说明

本项目使用标准的Scrapy项目结构，便于扩展和维护。您可以：

1. 在 `items.py` 中定义更详细的数据字段
2. 在 `pipelines.py` 中添加数据处理逻辑
3. 在 `middlewares.py` 中实现自定义中间件

## 🤝 贡献

欢迎提交Issue和Pull Request，但请确保：
- 代码符合PEP8规范
- 提交前进行充分测试
- 遵守项目的开源协议

---

**再次提醒**：请合理使用本工具，遵守相关法律法规，尊重知识产权。
