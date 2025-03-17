import pandas as pd
import os

# 创建data目录（如果不存在）
os.makedirs('data', exist_ok=True)

# 创建示例数据
data = {
    'attraction_id': ['001', '002'],
    'english_keywords': ['tianyi ge', 'westlake']
}

# 创建DataFrame
df = pd.DataFrame(data)

# 保存为Excel文件
excel_path = 'data/keywords.xlsx'
df.to_excel(excel_path, index=False)

print(f'已创建示例Excel文件：{excel_path}') 