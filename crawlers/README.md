# 播客爬虫工具

本目录包含用于从网易云音乐爬取播客内容的爬虫脚本。

## 文件说明

- `wasai.py` - 挖赛播客爬虫（参考实现）
- `suancai.py` - 新闻酸菜馆播客爬虫

## 依赖安装

```bash
pip install requests
```

## 使用方法

### 1. 运行 suancai.py 爬取新闻酸菜馆播客

```bash
python suancai.py
```

### 2. 运行 wasai.py 爬取挖赛播客

```bash
python wasai.py
```

## 功能特性

两个爬虫具有相同的处理流程：

1. **搜索播客** - 根据关键词在网易云音乐中搜索播客
2. **获取播客信息** - 获取播客的基本信息（名称、描述、节目总数等）
3. **爬取节目列表** - 分页获取所有节目信息
4. **解析节目数据** - 提取关键信息：
   - 节目ID
   - 节目名称
   - 节目描述
   - 发布时间
   - 时长
   - 收听次数
   - 点赞数
   - 评论数
   - 音频链接
   - 封面链接
5. **数据导出** - 支持两种格式：
   - JSON格式（方便程序处理）
   - Markdown格式（方便阅读）

## 输出文件

### suancai.py 输出

- `suancai_programs.json` - JSON格式的节目数据
- `suancai_programs.md` - Markdown格式的节目列表

### wasai.py 输出

- `wasai_programs.json` - JSON格式的节目数据
- `wasai_programs.md` - Markdown格式的节目列表

## 代码示例

### 基本使用

```python
from suancai import SuancaiCrawler

# 创建爬虫实例
crawler = SuancaiCrawler()

# 搜索播客
podcast_id = crawler.search_podcast("新闻酸菜馆")

# 爬取所有节目
programs = crawler.crawl_all_programs(podcast_id)

# 保存数据
crawler.save_to_json(programs, "output.json")
crawler.generate_markdown(programs, "output.md")
```

### 手动指定播客ID

如果你已经知道播客的ID，可以直接指定：

```python
from suancai import SuancaiCrawler

crawler = SuancaiCrawler()
crawler.podcast_id = "你的播客ID"

programs = crawler.crawl_all_programs()
crawler.save_to_json(programs)
```

## 注意事项

1. **请求频率** - 爬虫在请求之间会自动添加1秒延迟，避免请求过快
2. **网络连接** - 需要能够访问 music.163.com
3. **API变化** - 网易云音乐的API可能会发生变化，如果爬虫失效，需要更新API端点
4. **播客ID** - 某些播客可能需要手动指定ID，可以从网易云音乐网页版获取

## 数据结构

### 节目数据格式（JSON）

```json
{
  "id": "节目ID",
  "name": "节目标题",
  "description": "节目描述",
  "create_time": "2025-01-01 12:00:00",
  "duration": 3600,
  "duration_formatted": "01:00:00",
  "listen_count": 1000,
  "like_count": 50,
  "comment_count": 10,
  "audio_url": "音频文件URL",
  "cover_url": "封面图片URL"
}
```

## 相关链接

- [网易云音乐](https://music.163.com/)
- [StreamMusic 项目](https://github.com/gitbobobo/StreamMusic)

## 许可证

本项目遵循主项目的许可证。

## 免责声明

本爬虫仅供学习和研究使用，请遵守网易云音乐的服务条款和相关法律法规。禁止用于商业用途或任何违法行为。
