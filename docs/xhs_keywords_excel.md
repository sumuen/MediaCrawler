# 小红书关键词Excel搜索功能

## 功能介绍

MediaCrawler现在支持从Excel文件中读取关键词和景点ID，用于小红书搜索爬取。这个功能允许您批量管理搜索关键词，并将景点ID与搜索结果关联起来。

## 使用方法

1. 准备一个Excel文件，包含以下列：
   - `attraction_id`: 景点ID列，可以是任何标识景点的字符串
   - `english_keywords`: 英文关键词列，用于搜索小红书内容

2. 将Excel文件保存为`data/keywords.xlsx`

3. 运行爬虫命令：
   ```bash
   python main.py --platform xhs --lt qrcode --type search
   ```

4. 系统会自动读取Excel文件中的关键词，并将对应的景点ID写入到爬取的数据中

## 示例Excel文件

您可以运行以下命令生成示例Excel文件：
```bash
python create_example_excel.py
```

生成的示例文件结构如下：

| attraction_id | english_keywords |
|--------------|------------------|
| 001          | tianyi ge        |
| 002          | westlake         |

## 注意事项

1. 如果`data/keywords.xlsx`文件不存在，系统会使用配置文件`config/base_config.py`中的`KEYWORDS`配置项
2. Excel文件必须包含`attraction_id`和`english_keywords`两列
3. 爬取的数据会包含一个额外的`attraction_id`字段，用于关联景点信息
4. 确保Excel文件中的关键词是有效的搜索词，最好使用英文关键词以获得更好的搜索结果 